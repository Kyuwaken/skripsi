from rest_framework import viewsets
from ..serializers import TransactionResponseSerializer
from ..models import Transaction
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class TransactionViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionResponseSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)