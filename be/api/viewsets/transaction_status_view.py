from rest_framework import viewsets
from ..serializers import TransactionStatusSerializer, TransactionStatusResponseSerializer
from ..models import TransactionStatus
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

class TransactionStatusViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionStatusSerializer
    queryset = TransactionStatus.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('transaction','masterStatus')
        serializer = TransactionStatusResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            transaction_status =  self.queryset.get(pk=kwargs['pk']).select_related('transaction','masterStatus')
        except ObjectDoesNotExist:
            raise NotFoundException("Transaction Status")
        serializer = TransactionStatusResponseSerializer(transaction_status, many=False)
        return Response(serializer.data,status=200)