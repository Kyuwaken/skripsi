from rest_framework import serializers
from .category_serializer import CategorySerializer
from .user_serializer import UserSerializer
from ..models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductResponseSerializer(serializers.ModelSerializer):
    categoryId = CategorySerializer(many=False)
    sellerId = UserSerializer(many=False)
    class Meta:
        model = Product
        fields = '__all__'