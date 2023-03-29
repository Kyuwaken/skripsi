from rest_framework import viewsets
from ..serializers import PaymentTypeSerializer
from ..models import PaymentType
from api.permissions import IsAuthenticated
from api.utils import custom_viewset

class PaymentTypeViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = PaymentTypeSerializer
    queryset = PaymentType.objects.all()
    permission_classes = (IsAuthenticated,)