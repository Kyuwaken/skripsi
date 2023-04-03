from rest_framework import serializers
from .product_serializer import ProductResponseSerializer
from .user_serializer import  UserSerializer
from ..models import ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

class ProductReviewResponseSerializer(serializers.ModelSerializer):
    customer = UserSerializer(many=False)
    product = ProductResponseSerializer(many=False)
    class Meta:
        model = ProductReview
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None