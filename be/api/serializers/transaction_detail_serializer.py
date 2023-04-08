from rest_framework import serializers
from .product_serializer import ProductResponseImageSerializer,ProductResponseSerializer
from .user_serializer import UserSerializer
from ..models import TransactionDetail, Transaction

class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = '__all__'

class TransactionResponseSerializer(serializers.ModelSerializer):
    seller = UserSerializer(many=False)
    customer = UserSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionDetailResponseSerializer(serializers.ModelSerializer):
    transaction = TransactionResponseSerializer(many=False)
    product = ProductResponseImageSerializer(many=False)
    total = serializers.SerializerMethodField()
    class Meta:
        model = TransactionDetail
        fields = '__all__'
    
    def get_total(self,obj):
        return obj.quantity * obj.productPrice
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None

class TransactionDetailNotificationSerializer(serializers.ModelSerializer):
    transaction = TransactionResponseSerializer(many=False)
    product = ProductResponseSerializer(many=False)
    total = serializers.SerializerMethodField()
    class Meta:
        model = TransactionDetail
        fields = '__all__'
    
    def get_total(self,obj):
        return obj.quantity * obj.productPrice
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None