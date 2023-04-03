from rest_framework import serializers
from .transaction_serializer import TransactionResponseSerializer
from .product_serializer import ProductResponseSerializer
from ..models import TransactionDetail

class TransactionDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetail
        fields = '__all__'

class TransactionDetailResponseSerializer(serializers.ModelSerializer):
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