from .user_serializer import UserResponseSerializer
from .product_serializer import ProductResponseImageSerializer
from rest_framework import serializers
from ..models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'


class CartResponseSerializer(serializers.ModelSerializer):
    user = UserResponseSerializer(many=False)
    product = ProductResponseImageSerializer(many=False)
    class Meta:
        model = Cart
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None