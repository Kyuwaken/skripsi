from rest_framework import viewsets
from ..serializers import TransactionDetailResponseSerializer
from ..models import TransactionDetail
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class TransactionDetailViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionDetailResponseSerializer
    queryset = TransactionDetail.objects.all()
    permission_classes = (IsAuthenticated,)