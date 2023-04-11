from rest_framework import serializers
from .user_serializer import UserResponseSerializer
from .transaction_detail_serializer import TransactionDetailResponseSerializer, TransactionDetailNotificationSerializer
from .transaction_status_serializer import TransactionStatusResponseSerializer
from .payment_serializer import PaymentResponseSerializer
from ..models import Transaction, TransactionDetail, TransactionStatus, Payment


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionResponseSerializer(serializers.ModelSerializer):
    seller = UserResponseSerializer(many=False)
    customer = UserResponseSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'

class TransactionResponseDetailSerializer(serializers.ModelSerializer):
    seller = UserResponseSerializer(many=False)
    transaction_detail = TransactionDetailResponseSerializer(many=True)
    transaction_status = TransactionStatusResponseSerializer(many=True)
    payment = PaymentResponseSerializer(many=True)
    customer = UserResponseSerializer(many=False)
    class Meta:
        model = Transaction
        fields = ['id','seller','customer','noResi','preOrderTime','courierName',
                  'courierPrice','address','created_at','updated_at',
                  'created_by','updated_by', 'is_deleted','deleted_at',
                  'transaction_detail','transaction_status','payment']
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None

class TransactionResponseNotificationSerializer(serializers.ModelSerializer):
    seller = UserResponseSerializer(many=False)
    transaction_detail = TransactionDetailNotificationSerializer(many=True)
    transaction_status = TransactionStatusResponseSerializer(many=True)
    payment = PaymentResponseSerializer(many=True)
    customer = UserResponseSerializer(many=False)
    class Meta:
        model = Transaction
        fields = ['id','seller','customer','noResi','preOrderTime','courierName',
                  'courierPrice','address','created_at','updated_at',
                  'created_by','updated_by', 'is_deleted','deleted_at',
                  'transaction_detail','transaction_status','payment']
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None