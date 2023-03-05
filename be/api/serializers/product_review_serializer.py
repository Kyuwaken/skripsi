from rest_framework import serializers
from .product_serializer import ProductResponseSerializer
from .user_serializer import  UserSerializer
from ..models import ProductReview


class ProductReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductReview
        fields = '__all__'

class ProductReviewResponseSerializer(serializers.ModelSerializer):
    customerId = UserSerializer(many=False)
    productId = ProductResponseSerializer(many=False)
    class Meta:
        model = ProductReview
        fields = '__all__'