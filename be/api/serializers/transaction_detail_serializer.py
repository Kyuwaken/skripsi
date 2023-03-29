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
    class Meta:
        model = TransactionDetail
        fields = '__all__'