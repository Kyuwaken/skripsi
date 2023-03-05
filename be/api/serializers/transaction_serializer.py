from rest_framework import serializers
from .user_serializer import UserSerializer
from ..models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
    

class TransactionResponseSerializer(serializers.ModelSerializer):
    sellerId = UserSerializer(many=False)
    customerId = UserSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'