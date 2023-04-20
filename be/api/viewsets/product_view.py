from rest_framework import viewsets
from ..serializers import ProductSerializer, ProductResponseSerializer, ProductImageSerializer, ProductResponseImageSerializer
from rest_framework.response import Response
from ..models import Product, ProductImage
from api.permissions import IsAuthenticated, IsSellerOrReadOnly
from api.exceptions import NotAuthorizedException,NotFoundException
from django.db.models.base import ObjectDoesNotExist
from api.utils import custom_viewset
from rest_framework.decorators import action
from api.utils.validation_input import validate_integer, validate_input
from api.exceptions import NotAuthorizedException,NotFoundException, ValidationException
import base64, copy, os
from django.db import transaction

class ProductViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated, IsSellerOrReadOnly)

    def validate_max_size(self,request):
        print(request.data)
        temp = copy.deepcopy(request.data)
        data = temp.pop('productPhoto')
        print("ini data : " + str(data))
        for i in data:
            print(i)
            if i.size > 1000000:
                raise ValidationException("Size must less than 1 MB")
    
    def validate_type_file(self,request):
        temp = copy.deepcopy(request.data)
        data = temp.pop('productPhoto')
        for i in data:
            name = i._name
            arr = name.split('.')
            index = len(arr)-1
            if arr[index].strip() not in ['png','jpg','jpeg']:
                raise ValidationException("Must input image type png or jpg or jpeg")

    def list(self, request):
        queryset = self.queryset.filter(is_deleted=False).select_related('category').prefetch_related('product_image')
        serializer = ProductResponseImageSerializer(queryset, many=True)
        return Response(serializer.data, status=200)

    @action(detail=False, methods=['post'], url_path='seller')
    def get_by_seller_id(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        queryset = self.queryset.filter(seller_id=request.data['id']).select_related('category').prefetch_related('product_image')
        serializer = ProductResponseImageSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    @action(detail=False, methods=['get'], url_path='list-with-image')
    def list_with_image(self, request):
        queryset = self.queryset.select_related('category').prefetch_related('product_image')
        serializer = ProductResponseSerializer(queryset, many=True)
        data = copy.deepcopy(serializer.data)
        
        images = ProductImage.objects.all()
        image_path = {}
        for i in images:
            if i.product.id not in image_path:
                image_path[i.product.id] = i.productPhoto.path
        for i in data:
            image = {}
            path = image_path[i['id']]
            with open(path,'rb') as img_file:
                extension = str(path).split('.')[-1].lower()
                b64_string = base64.b64encode(img_file.read())
                image['id'] = i['id']
                image['path'] = path
                image['imageType']= "image/"+extension
                image['stringBase64'] = b64_string
            i['product_image'] = image
        return Response(data, status=200)
    
    @action(detail=False, methods=['post'], url_path='get-by-category')
    def getByCategory(self, request, *args, **kwargs):
        validate_integer(request.data,['id'])
        category_id = request.data['id']
        queryset = self.queryset.filter(category_id=category_id).select_related('category')
        serializer = ProductResponseSerializer(queryset, many=True)
        data = copy.deepcopy(serializer.data)
        
        images = ProductImage.objects.all()
        image_path = {}
        for i in images:
            if i.product.id not in image_path:
                image_path[i.product.id] = i.productPhoto.path
        for i in data:
            image = {}
            path = image_path[i['id']]
            with open(path,'rb') as img_file:
                extension = str(path).split('.')[-1].lower()
                b64_string = base64.b64encode(img_file.read())
                image['id'] = i['id']
                image['path'] = path
                image['imageType']= "image/"+extension
                image['stringBase64'] = b64_string
            i['product_image'] = image
        return Response(data, status=200)
    
    @action(detail=True, methods=['get'], url_path='retrieve-with-image')
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
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='create-product-with-image')
    def create_product_with_image(self, request, *args, **kwargs): 
        # breakpoint()
        print(request.data)
        # validate_input(request.data,['name','price','productDescription','productPhoto'])
        product = Product.objects.filter(name__iexact = request.data['name'],seller_id=request.custom_user['id'])
        if product:
            raise ValidationException('Product ' + request.data['name'] + ' in seller '+ request.custom_user['name'] + ' already exists')
        # request.data._mutable=True
        request.data['seller']=request.custom_user['id']
        super().create(request, *args, **kwargs)
        product = Product.objects.get(name = request.data['name'],seller_id=request.custom_user['id'],price=request.data['price'])
        self.validate_max_size(request)
        self.validate_type_file(request)
        data = request.data.pop('productPhoto')
        for index,i in enumerate(data):
            last = str(i.name).split('.')
            i.name = str(index+1) + '.'+last[-1]
            ProductImage.objects.create(productPhoto=i,product_id=product.id)
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
    
    @transaction.atomic
    def update(self, request, *args, **kwargs):
        try:
            product = self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Product")
        self.validate_max_size(request)
        self.validate_type_file(request)
        data = request.data.pop('productPhoto')
        product_images = ProductImage.objects.filter(product_id=kwargs['pk'])
        path = []
        for i in product_images:
            path.append(i.productPhoto.path)
        product_images.delete()
        for i in path:
            if os.path.isfile(i):
                os.remove(i)
        for index,i in enumerate(data):
            last = str(i.name).split('.')
            i.name = str(index+1) + '.'+last[-1]
            ProductImage.objects.create(productPhoto=i,product_id=product.id)
        return Response(status=200)
    def destroy(self, request, *args, **kwargs):
        product_images = ProductImage.objects.filter(product_id=kwargs['pk'])
        path = []
        for i in product_images:
            path.append(i.productPhoto.path)
        product_images.delete()
        for i in path:
            if os.path.isfile(i):
                os.remove(i)
        return super().destroy(request, *args, **kwargs)
    

    
