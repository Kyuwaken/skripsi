from .user_serializer import UserSerializer
from .product_serializer import ProductResponseSerializer
from rest_framework import serializers
from ..models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartResponseSerializer(serializers.ModelSerializer):
    userId = UserSerializer(many=False)
    productId = ProductResponseSerializer(many=False)
    class Meta:
        model = Cart
        fields = '__all__'