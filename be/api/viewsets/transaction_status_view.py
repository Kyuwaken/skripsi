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
        transaction_id = request.data['id']
        master_status = self.queryset.filter(transaction_id=transaction_id).order_by('-id')[0].masterStatus
        serz = MasterStatusSerializer(master_status,many=False)
        return Response(serz.data,status=200)
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='update-status-transaction')
    def updateStatusTransaction(self, request):
        transaction_id = request.data['transaction']
        masterStatus_id = request.data['masterStatus']
        master_status = self.queryset.filter(transaction_id=transaction_id).order_by('-id')[0].masterStatus.id
        if master_status > masterStatus_id : raise ValidationException("status transaction cannot go back")
        if masterStatus_id > 12: raise ValidationException('max status transaction cannot update more')
        if masterStatus_id == 2:
            send_notification('NO REPLY - CONFIRMATION PRODUCTS - [NAMEAPPS]' ,transaction_id, 'confirmation_product')
            send_notification('NO REPLY - BUY THE PRODUCTS - [NAMEAPPS]' ,transaction_id, 'seller_buy_product')
        if masterStatus_id == 7:
            send_notification('NO REPLY - TRANSACTION REJECTED BY SELLER - [NAMEAPPS]',transaction_id,'seller_reject_transaction')
        if masterStatus_id == 3: # antara taruh sini atau bikin di transaction tergantung inputnya apa
            send_notification('NO REPLY - NEED FULL PAYMENT - [NAMEAPPS]',transaction_id,'to_full_payment')
        transactionStatus = TransactionStatus.objects.create(transaction_id=transaction_id, masterStatus_id=masterStatus_id)
        serz = TransactionStatusResponseSerializer(transactionStatus,many=False)
        return Response(serz.data,status=200)