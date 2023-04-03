from rest_framework import viewsets
from ..serializers import TransactionSerializer,TransactionResponseSerializer
from ..models import Transaction, Product, User, TransactionDetail, Payment, TransactionStatus
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response
from rest_framework.decorators import action
import copy, datetime

class TransactionViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('user')
        serializer = TransactionResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            transaction =  self.queryset.get(pk=kwargs['pk']).select_related('user')
        except ObjectDoesNotExist:
            raise NotFoundException("Transaction")
        serializer = TransactionResponseSerializer(transaction, many=False)
        return Response(serializer.data,status=200)
    
    # create transaction, banyak transaction detail tergantung barang dan status transaksi, 1 payment
    # total ada lebih dari 1 transaction detail, 2 payment yaitu DP dan FP
    def create(self, request, *args, **kwargs):
        customer = request.custom_user['id']
        products = request.data['product'].pop()
        payment_method = request.data['payment_method']
        tr_detail = []
        for i in products:
            if i == 0: seller = Product.objects.get(pk=i['product_id']).seller.id
            detail = {}
            product = i['product_id']
            product_price = i['product_price']
            quantity = i['quantity']
            detail['product_id'] = product
            detail['product_price'] = product_price
            detail['quantity'] = quantity
            tr_detail.append(copy.deepcopy(detail))
        transaction = Transaction.objects.create(cutomer_id = customer, seller_id = seller)
        serz = TransactionSerializer(transaction,many=False)
        id_transaction = serz.data['id']
        for i in tr_detail:
            transaction_detail = TransactionDetail.objects.create(transaction_id=id_transaction,**i)
        transaction_status = TransactionStatus.objects.create(transaction_id=id_transaction, masterStatus_id=1)
        payment = Payment.objects.create(transaction_id=id_transaction, paymentType_id=1, paymentMethod_id=payment_method, paymentStatus=1)
        return Response(status=200)
    
    # create job that already status already bought by seller, waiting to be fully paid by customer after 3 days auto cancel
    # by filter all the transaction that still in that status and checking that ordered+3 days > date now means auto cancel
    @action(detail=False, methods=['get'], url_name='checking-due-date-full-payment')
    def job_checking_due_date_full_payment(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=4)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 4]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=4).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered + datetime.timedelta(days=3) > datetime.datetime.now():
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus=6)
        return Response(status=200)
    
    # create job that cancel the order because the seller pre order is time limit
    @action(detail=False, methods=['get'], url_name='checking-time-limit-seller-preorder')
    def job_checking_time_limit_seller_preorder(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=2)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 2]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=2).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered + datetime.timedelta(days=i.transaction.preOrderTime) > datetime.datetime.now():
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus=5)
        return Response(status=200)

    
