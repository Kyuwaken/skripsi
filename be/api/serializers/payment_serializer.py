from rest_framework import serializers
from .payment_type_serializer import PaymentTypeSerializer
from .payment_method_serializer import PaymentMethodSerializer
from .user_serializer import UserResponseSerializer
from ..models import Payment, Transaction

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class TransactionResponseSerializer(serializers.ModelSerializer):
    seller = UserResponseSerializer(many=False)
    customer = UserResponseSerializer(many=False)
    class Meta:
        model = Transaction
        fields = '__all__'

class PaymentResponseSerializer(serializers.ModelSerializer):
    transaction = TransactionResponseSerializer(many=False)
    paymentType = PaymentTypeSerializer(many=False)
    paymentMethod = PaymentMethodSerializer(many=False)
    class Meta:
        model = Payment
        fields = '__all__'
        
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None