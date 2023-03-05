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
    transactionId = TransactionSerializer(many=False)
    paymentTypeId = PaymentTypeSerializer(many=False)
    paymentMethodId = PaymentMethodSerializer(many=False)
    class Meta:
        model = Payment
        fields = '__all__'