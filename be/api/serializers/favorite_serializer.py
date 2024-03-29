from .user_serializer import UserSerializer
from .product_serializer import ProductResponseImageSerializer
from rest_framework import serializers
from ..models import Favorite

class FavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorite
        fields = '__all__'

class FavoriteResponseSerializer(serializers.ModelSerializer):
    product = ProductResponseImageSerializer(many=False)
    user = UserSerializer(many=False)
    class Meta:
        model = Favorite
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None