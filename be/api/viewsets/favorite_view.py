from rest_framework import viewsets
from ..serializers import FavoriteSerializer, FavoriteResponseSerializer, ProductResponseImageSerializer
from ..models import Favorite, Product
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException, ValidationException
from rest_framework.response import Response
from rest_framework.decorators import action
from api.utils.validation_input import validate_integer, validate_input
import copy

class FavoriteViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = FavoriteSerializer
    queryset = Favorite.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('user','product')
        serializer = FavoriteResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            favorite =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Favorite")
        serializer = FavoriteResponseSerializer(favorite, many=False)
        return Response(serializer.data,status=200)
    
    def create(self, request, *args, **kwargs):
        validate_input(request.data,['user','product'])
        try:
            favorite = self.queryset.get(user_id=request.data['user'],product_id=request.data['product'])
            favorite.delete()
        except:
            favorite = self.queryset.create(user_id=request.data['user'],product_id=request.data['product'])
        product = Product.objects.get(pk=request.data['product'])
        serializer = ProductResponseImageSerializer(product,many=False)
        data = copy.deepcopy(serializer.data)
        try:
            favorite = Favorite.objects.get(user_id=request.data['user'],product_id=request.data['product'])
            data['favorite'] = True
        except:
            data['favorite'] = False
        return Response(data, status=200)
    
    @action(detail=False, methods=['post'], url_path='user')
    def get_favorite_by_id(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        products = [i.product for i in self.queryset.filter(user_id=request.data['id'])]
        serializer = ProductResponseImageSerializer(products, many=True)
        return Response(serializer.data,status=200)