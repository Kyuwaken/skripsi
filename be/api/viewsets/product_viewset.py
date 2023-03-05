from rest_framework import viewsets
from ..serializers import ProductSerializer
from rest_framework.response import Response
from ..models import Product
from api.permissions import IsAuthenticated, IsSellerOrReadOnly
from api.exceptions import NotAuthorizedException,NotFoundException
from django.db.models.base import ObjectDoesNotExist

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    # permission_classes = (IsAuthenticated, IsSellerOrReadOnly)

    # def create(self, request, *args, **kwargs):
    #     if role_id =='Seller':
    #         return super().create(request, *args, **kwargs)
    #     else:
    #         return NotAuthorizedException()

    def list(self, request):
        queryset = self.queryset.select_related('categoryId')
        serializer = ProductSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            product =  self.queryset.get(pk=kwargs['pk']).select_related('categoryId')
        except ObjectDoesNotExist:
            raise NotFoundException("Product")
        serializer = ProductSerializer(product, many=False)
        return Response(serializer.data,status=200)