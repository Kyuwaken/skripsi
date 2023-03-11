from rest_framework import viewsets
from ..serializers import PaymentMethodSerializer
from ..models import PaymentMethod
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class PaymentMethodViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = PaymentMethodSerializer
    queryset = PaymentMethod.objects.all()
    permission_classes = (IsAuthenticated,)