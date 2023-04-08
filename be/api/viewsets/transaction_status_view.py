from rest_framework import viewsets
from ..serializers import TransactionStatusSerializer, TransactionStatusResponseSerializer, MasterStatusSerializer
from ..models import TransactionStatus
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException, ValidationException
from rest_framework.response import Response
from rest_framework.decorators import action
from api.utils.send_email_util import send_notification
from django.db import transaction

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
    
    @action(detail=False, methods=['post'], url_path='check-status-transaction')
    def checkStatusTransaction(self, request):
        transaction_id = request.data['transaction']
        breakpoint()
        master_status = self.queryset.filter(transaction_id=transaction_id).order_by('-id')[0].masterStatus
        serz = MasterStatusSerializer(master_status,many=False)
        return Response(serz.data,status=200)
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='update-status-transaction')
    def updateStatusTransaction(self, request):
        transaction_id = request.data['transaction']
        masterStatus_id = request.data['masterStatus']
        if masterStatus_id > 8: raise ValidationException('max status transaction cannot update more')
        if masterStatus_id == 2:
            send_notification('NO REPLY - ALREADY PAY DP - [NAMEAPPS]' ,transaction_id, 'already_pay_dp')
            send_notification('NO REPLY - TO BE CONFIRM - [NAMEAPPS]',transaction_id, 'product_to_be_confirm')
        
        transactionStatus = TransactionStatus.objects.create(transaction_id=transaction_id, masterStatus_id=masterStatus_id)
        serz = TransactionStatusResponseSerializer(transactionStatus,many=False)
        return Response(serz.data,status=200)