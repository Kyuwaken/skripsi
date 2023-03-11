from rest_framework import serializers
from .transaction_serializer import TransactionResponseSerializer
from .master_status_serializer import MasterStatusSerializer
from ..models import TransactionStatus

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = '__all__'

class TransactionStatusResponseSerializer(serializers.ModelSerializer):
    transaction = TransactionResponseSerializer(many=False)
    masterStatus = MasterStatusSerializer(many=False)
    class Meta:
        model = TransactionStatus
        fields = '__all__'