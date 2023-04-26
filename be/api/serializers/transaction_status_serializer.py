from rest_framework import serializers
from .master_status_serializer import MasterStatusSerializer
from .user_serializer import UserResponseSerializer
from ..models import TransactionStatus, Transaction

class TransactionStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionStatus
        fields = '__all__'

class TransactionResponseSerializer(serializers.ModelSerializer):
    seller = UserResponseSerializer(many=False)
    customer = UserResponseSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionStatusResponseSerializer(serializers.ModelSerializer):
    transaction = TransactionResponseSerializer(many=False)
    masterStatus = MasterStatusSerializer(many=False)
    class Meta:
        model = TransactionStatus
        fields = '__all__'
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None