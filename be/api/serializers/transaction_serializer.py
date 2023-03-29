from rest_framework import serializers
from .user_serializer import UserSerializer
from ..models import Transaction


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'
    

class TransactionResponseSerializer(serializers.ModelSerializer):
    seller = UserSerializer(many=False)
    customer = UserSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'