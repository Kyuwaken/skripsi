from .user_serializer import UserSerializer
from .product_serializer import ProductSerializer
from rest_framework import serializers
from ..models import Favourite

class FavouriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favourite
        fields = '__all__'

class FavouriteResponseSerializer(serializers.ModelSerializer):
    productId = ProductSerializer(many=False)
    userId = UserSerializer(many=False)
    class Meta:
        model = Favourite
        fields = '__all__'