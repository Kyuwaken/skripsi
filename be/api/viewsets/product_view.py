from rest_framework import viewsets
from ..serializers import ProductSerializer, ProductResponseSerializer
from rest_framework.response import Response
from ..models import Product
from api.permissions import IsAuthenticated, IsSellerOrReadOnly
from api.exceptions import NotAuthorizedException,NotFoundException
from django.db.models.base import ObjectDoesNotExist
from api.utils import custom_viewset

class ProductViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    # permission_classes = (IsAuthenticated, IsSellerOrReadOnly)

    def list(self, request):
        queryset = self.queryset.select_related('category')
        serializer = ProductResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            product =  self.queryset.get(pk=kwargs['pk']).select_related('category')
        except ObjectDoesNotExist:
            raise NotFoundException("Product")
        serializer = ProductResponseSerializer(product, many=False)
        return Response(serializer.data,status=200)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)