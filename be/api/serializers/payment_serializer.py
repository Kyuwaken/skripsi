from rest_framework import serializers
from .transaction_serializer import TransactionSerializer
from .payment_type_serializer import PaymentTypeSerializer
from .payment_method_serializer import PaymentMethodSerializer
from ..models import Payment

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'

class PaymentResponseSerializer(serializers.ModelSerializer):
    transaction = TransactionSerializer(many=False)
    paymentType = PaymentTypeSerializer(many=False)
    paymentMethod = PaymentMethodSerializer(many=False)
    class Meta:
        model = Payment
        fields = '__all__'