from rest_framework import viewsets
from ..serializers import PaymentResponseSerializer
from ..models import Payment
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class PaymentViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = PaymentResponseSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)