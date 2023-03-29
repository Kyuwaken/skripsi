from rest_framework import serializers
from .category_serializer import CategorySerializer
from .user_serializer import UserSerializer
from ..models import Product, ProductImage


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductResponseSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    seller = UserSerializer(many=False)
    class Meta:
        model = Product
        fields = '__all__'

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['id','productPhoto']

class ProductResponseImageSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)
    product_image = ProductImageSerializer(many=True)
    seller = UserSerializer(many=False)
    class Meta:
        model = Product
        fields = ['id','name','category','seller',
                  'price','preorderTime','productDescription',
                  'created_at','updated_at','created_by','updated_by',
                  'is_deleted','deleted_at','product_image']