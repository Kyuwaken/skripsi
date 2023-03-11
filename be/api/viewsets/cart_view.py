from rest_framework import viewsets
from ..serializers import CartSerializer,CartResponseSerializer
from ..models import Cart
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

class CartViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('user','product')
        serializer = CartResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            cart =  self.queryset.get(pk=kwargs['pk']).select_related('user','product')
        except ObjectDoesNotExist:
            raise NotFoundException("Cart")
        serializer = CartResponseSerializer(cart, many=False)
        return Response(serializer.data,status=200)