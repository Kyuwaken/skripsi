from rest_framework import viewsets
from ..serializers import CartSerializer,CartResponseSerializer
from ..models import Cart
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response
from rest_framework.decorators import action
from api.utils.validation_input import validate_integer, validate_input
from django.db import transaction

class CartViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        pass
    
    def retrieve(self, request, *args, **kwargs):
        pass
    
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        validate_input(request.data,['user','product'])
        try:
            cart = self.queryset.get(user_id=request.data['user'],product_id=request.data['product'])
        except:
            cart = []
        if cart:
            cart.quantity = int(cart.quantity) + 1
            cart.save()
        else:
            cart = self.queryset.create(user_id=request.data['user'],product_id=request.data['product'],quantity=1)
        serializer = CartSerializer(cart,many=False)    
        return Response(serializer.data, status=200)
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='decrease-quantity')
    def decreate_quantity(self, request, *args, **kwargs):
        validate_input(request.data,['user','product'])
        try:
            cart = self.queryset.get(user_id=request.data['user'],product_id=request.data['product'])
        except:
            raise NotFoundException("Cart")
        cart.quantity = int(cart.quantity) - 1
        cart.save()
        serializer = CartResponseSerializer(cart, many=False)
        return Response(serializer.data,status=200)
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='custom-quantity')
    def custom_quantity(self, request, *args, **kwargs):
        validate_input(request.data,['user','product','quantity'])
        try:
            cart = self.queryset.get(user_id=request.data['user'],product_id=request.data['product'])
        except:
            raise NotFoundException("Cart")
        cart.quantity = request.data['quantity']
        cart.save()
        serializer = CartResponseSerializer(cart, many=False)
        return Response(serializer.data,status=200)
    
    @action(detail=False, methods=['post'], url_path='user')
    def get_cart_by_id(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        cart = self.queryset.filter(user_id=request.data['id'])
        serializer = CartResponseSerializer(cart, many=True)
        return Response(serializer.data,status=200)
