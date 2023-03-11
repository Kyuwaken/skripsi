from rest_framework import viewsets
from ..serializers import TransactionStatusResponseSerializer
from ..models import TransactionStatus
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class TransactionStatusViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionStatusResponseSerializer
    queryset = TransactionStatus.objects.all()
    permission_classes = (IsAuthenticated,)