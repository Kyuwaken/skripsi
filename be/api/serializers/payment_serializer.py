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
        
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None