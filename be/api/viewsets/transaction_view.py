from rest_framework import viewsets
from ..serializers import TransactionSerializer,TransactionResponseSerializer, PaymentSerializer, TransactionResponseDetailSerializer
from ..models import Transaction, Product, User, TransactionDetail, Payment, TransactionStatus
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response
from rest_framework.decorators import action
import copy, datetime
from api.utils.validation_input import validate_input
from django.db import transaction

class TransactionViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('seller','customer')
        serializer = TransactionResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            transaction =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Transaction")
        serializer = TransactionResponseDetailSerializer(transaction, many=False)
        return Response(serializer.data,status=200)
    
    # create transaction, banyak transaction detail tergantung barang dan status transaksi, 1 payment
    # total ada lebih dari 1 transaction detail, 2 payment yaitu DP dan FP
    @transaction.atomic
    def create(self, request, *args, **kwargs):
        validate_input(request.data,['product','payment_method','address','nominal'])
        customer = request.custom_user['id']
        products = request.data['product']
        del request.data['product']
        payment_method = request.data['payment_method']
        address = request.data['address']
        nominal = request.data['nominal']
        preOrderTime = 0
        # tr_detail = []
        for index,i in enumerate(products):
            if index == 0: seller = Product.objects.get(pk=i['product_id']).seller.id
            if preOrderTime<i['preorderTime']: preOrderTime = i['preorderTime']
            # detail = {}
            # product = i['product_id']
            # product_price = i['product_price']
            # quantity = i['quantity']
            # detail['product_id'] = product
            # detail['product_price'] = product_price
            # detail['quantity'] = quantity
            # tr_detail.append(copy.deepcopy(detail))
        transaction = Transaction.objects.create(customer_id = customer, seller_id = seller, address = address,preOrderTime=preOrderTime)
        serz = TransactionSerializer(transaction,many=False)
        id_transaction = serz.data['id']
        for i in products:
            transaction_detail = TransactionDetail.objects.create(transaction_id=id_transaction,**i)
        transaction_status = TransactionStatus.objects.create(transaction_id=id_transaction, masterStatus_id=1)
        payment = Payment.objects.create(transaction_id=id_transaction, paymentType_id=1, paymentMethod_id=payment_method, nominal=nominal)
        return Response(status=200)
    
    # create job that already status already bought by seller, waiting to be fully paid by customer after 3 days auto cancel
    # by filter all the transaction that still in that status and checking that ordered+3 days > date now means auto cancel
    @transaction.atomic
    @action(detail=False, methods=['get'], url_path='checking-due-date-full-payment')
    def job_checking_due_date_full_payment(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=4)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 4]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=4).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered.date() + datetime.timedelta(days=3) < datetime.datetime.now().date():
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus=6)
        return Response(status=200)
    
    # create job that cancel the order because the seller pre order is time limit
    @transaction.atomic
    @action(detail=False, methods=['get'], url_path='checking-time-limit-seller-preorder')
    def job_checking_time_limit_seller_preorder(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=2)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 2]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=2).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered.date() + datetime.timedelta(days=i.transaction.preOrderTime) < datetime.datetime.now().date():
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus=5)
        return Response(status=200)
    
    @action(detail=False, methods=['get'], url_path='checking-due-date-sending-product')
    @transaction.atomic
    def job_checking_due_date_sending_product(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=7)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 7]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=7).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered.date() + datetime.timedelta(days=3) < datetime.datetime.now().date():
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus=8)
        return Response(status=200)
    
    @action(detail=False, methods=['get'], url_path='checking-seller-confirmation')
    @transaction.atomic
    def job_checking_seller_confirmation(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=1)]
        breakpoint()
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 1]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=1).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered.date() + datetime.timedelta(days=3) < datetime.datetime.now().date():
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus=3)
        return Response(status=200)
    
    # @action(detail=False, methods=['post'], url_path='full-payment')
    # def transaction_full_payment(self, request, *args, **kwargs):
    #     validate_input(request.data,['transaction','paymentType','paymentMethod','nominal'])
    #     payment = Payment.objects.create(**request.data)
    #     serz = PaymentSerializer(payment,many=False)
    #     return Response(serz.data,status=200)

    @action(detail=False, methods=['post'], url_path='get-down-payment')
    def getDetailDownPayment(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        transactionDetail = TransactionDetail.objects.filter(transaction_id=request.data['id'])
        total = 0
        for i in transactionDetail:
            total += i.productPrice * i.quantity
        payment_dp = total * 20 / 100
        data = {
            "total": total,
            "dp": int(payment_dp)
        }
        return Response(data,status=200)
    
    @action(detail=False, methods=['post'], url_path='get-full-payment')
    def getDetailFullPayment(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        payment_dp = Payment.objects.get(transaction_id=request.data['id'],paymentType_id=1)
        transactionDetail = TransactionDetail.objects.filter(transaction_id=request.data['id'])
        total = 0
        for i in transactionDetail:
            total += i.productPrice * i.quantity
        grandTotal = total - payment_dp.nominal
        data = {
            "total": total,
            "dp": payment_dp.nominal,
            "grandTotal": grandTotal
        }
        return Response(data,status=200)
        

