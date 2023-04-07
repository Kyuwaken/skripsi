from rest_framework import serializers
from .category_serializer import CategorySerializer
from .user_serializer import UserSerializer
from ..models import Product, ProductImage
import base64


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
    imageType = serializers.SerializerMethodField()
    stringBase64 = serializers.SerializerMethodField()
    class Meta:
        model = ProductImage
        fields = ['id','imageType','stringBase64']
    def get_imageType(self,obj):
        with open(obj.productPhoto.path, 'rb') as img_file:
            extension = str(obj.productPhoto.path).split('.')[-1].lower()
            return "image/"+extension
    def get_stringBase64(self,obj):
        with open(obj.productPhoto.path, 'rb') as img_file:
            return base64.b64encode(img_file.read())

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
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None