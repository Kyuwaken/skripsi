from rest_framework import viewsets
from ..serializers import ProductSerializer, ProductResponseSerializer, ProductImageSerializer, ProductResponseImageSerializer
from rest_framework.response import Response
from ..models import Product, ProductImage
from api.permissions import IsAuthenticated, IsSellerOrReadOnly
from api.exceptions import NotAuthorizedException,NotFoundException
from django.db.models.base import ObjectDoesNotExist
from api.utils import custom_viewset
from rest_framework.decorators import action
from api.utils.validation_input import validate_integer
from api.exceptions import NotAuthorizedException,NotFoundException, ValidationException
import base64

class ProductViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, IsSellerOrReadOnly)

    def validate_max_size(self,request):
        dataExcel = request.data['productPhoto']
        if dataExcel.size > 1000000:
            raise ValidationException("Size excel must less than 1 MB")
    
    def validate_type_file(self,request):
        dataExcel = request.data['productPhoto']
        name = dataExcel._name
        arr = name.split('.')
        index = len(arr)-1
        if arr[index].strip() not in ['png','jpg','jpeg']:
            raise ValidationException("Must input image type png or jpg or jpeg")

    def list(self, request):
        queryset = self.queryset.select_related('category').prefetch_related('product_image')
        serializer = ProductResponseImageSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    @action(detail=True, methods=['get'])
    def retrieve_with_image(self, request, *args, **kwargs):
        try:
            product =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Product")
        serializer = ProductResponseSerializer(product, many=False)
        images = ProductImage.objects.filter(product__id = kwargs['pk'])
        image_resp = []
        for i in images:
            # breakpoint()
            image = {}
            path = i.productPhoto.path
            with open(path, 'rb') as img_file:
                extension = str(path).split('.')[-1].lower()
                b64_string = base64.b64encode(img_file.read())
                image['id'] = i.id
                image['path'] = path
                image['imageType']= "image/"+extension
                image['stringBase64'] = b64_string
            image_resp.append(image)
        data = serializer.data
        data['product_image'] = image_resp
        return Response(data,status=200)
    
    @action(detail=False, methods=['post'])
    def create_product_with_image(self, request, *args, **kwargs):
        product = super().create(request, *args, **kwargs)
        self.validate_max_size(request)
        self.validate_type_file(request)
        data = request.data['productPhoto']
        for i in data:
            ProductImage.objects.create(productPhoto=i,product=product)
        return Response(status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            product =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Product")
        serializer = ProductResponseImageSerializer(product, many=False)
            
        return Response(serializer.data,status=200)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'])
    def getByCategory(self, request, *args, **kwargs):
        validate_integer(request.data,['category'])
        category_id = request.data['category']
        queryset = self.queryset.filter(category_id=category_id).select_related('category')
        serializer = ProductResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    