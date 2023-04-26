from rest_framework import viewsets
from ..serializers import ProductImageSerializer
from ..models import ProductImage
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from rest_framework.decorators import action
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException, ValidationException
from rest_framework.response import Response
import base64
import os

class ProductImageViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = ProductImageSerializer
    queryset = ProductImage.objects.all()
    permission_classes = (IsAuthenticated,)

    # @action(detail=False, methods=['post'])
    # def getImage(self, request, *args, **kwargs):
    #     url = request.data['path']
    #     url_resp = requests.get(f'{url}', headers={'Authorization': 'HCP '+str(os.getenv('VUE_APP_HCP_KEY'))
    #     },verify= False, stream=True)
    #     url =
    #     resp = {}
    #     base = PVC().PATH
    #     name_file = url.split("//")[-1]
    #     with open('img.png', 'wb') as out_file:
    #         out_file.write(url_resp.content)

    #     with open('img.png', 'rb') as img_file:
    #         extension = str(request.data['path']).split('.')[-1].lower()
    #         b64_string = base64.b64encode(img_file.read())
    #         resp['imageType']= "image/"+extension
    #         resp['stringBase64'] = b64_string
    #     # os.remove('img.png')
    #     return Response(resp)
    def list(self, request, *args, **kwargs):
        queryset = self.queryset
        serializer = ProductImageSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            product_image =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Product Image")
        serializer = ProductImageSerializer(product_image, many=False)
        # url = product_image.image
        # with open('img.png', 'wb') as out_file:
            # out_file.write(url.content)
        # resp = {}
        # with open('img.png', 'rb') as img_file:
        #     extension = str(product_image.image.url).split('.')[-1].lower()
        #     b64_string = base64.b64encode(img_file.read())
        #     resp['imageType']= "image/"+extension
        #     resp['stringBase64'] = b64_string
        return Response(serializer.data,status=200)
        # serializer = ProductReviewResponseSerializer(product_image, many=False)
        # return Response(serializer.data,status=200)
        # pass
    
    def create(self, request, *args, **kwargs):
        self.validate_max_size(request)
        self.validate_type_file(request)
        return super().create(request, *args, **kwargs)
    
    def validate_max_size(self,request):
        dataExcel = request.data['image']
        if dataExcel.size > 1000000:
            raise ValidationException("Size excel must less than 1 MB")
    
    def validate_type_file(self,request):
        dataExcel = request.data['image']
        name = dataExcel._name
        arr = name.split('.')
        index = len(arr)-1
        if arr[index].strip() not in ['png','jpg','jpeg']:
            raise ValidationException("Must input image type png or jpg or jpeg")
    
    def destroy(self, request, *args, **kwargs):
        id = kwargs['pk']
        data = ProductImage.objects.get(pk=id).image
        if data:
            if os.path.isfile(data.path):
                os.remove(data.path)
        return super().destroy(request, *args, **kwargs)