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
from api.utils.send_email_util import send_notification

class TransactionViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionSerializer
    queryset = Transaction.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('seller','customer')
        serializer = TransactionResponseSerializer(queryset, many=True)
        data = copy.deepcopy(serializer.data)
        for i in data:
            if i['readyAt']: 
                date =  datetime.datetime.strptime(i['readyAt'],'%Y-%m-%dT%H:%M:%S%z')
                i['readyAt']=date.strftime("%d %B %Y")

        return Response(data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            transaction =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Transaction")
        serializer = TransactionResponseDetailSerializer(transaction, many=False)
        data = copy.deepcopy(serializer.data)
        if data['readyAt']:
            date =  datetime.datetime.strptime(data['readyAt'],'%Y-%m-%dT%H:%M:%S%z')
            data['readyAt']=date.strftime("%d %B %Y")
        return Response(data,status=200)
    
    @action(detail=False, methods=['get'], url_path='seller')
    def getAllTransactionByIdSeller(self, request, *args, **kwargs):
        queryset = self.queryset.filter(seller_id=request.custom_user['id'])
        serializer = TransactionResponseDetailSerializer(queryset, many=True)
        data = copy.deepcopy(serializer.data)
        for i in data:
            if i['readyAt']: 
                date =  datetime.datetime.strptime(i['readyAt'],'%Y-%m-%dT%H:%M:%S%z')
                i['readyAt']=date.strftime("%d %B %Y")
        return Response(data,status=200)
    
    @action(detail=False, methods=['get'], url_path='customer')
    def getAllTransactionByIdCustomer(self, request, *args, **kwargs):
        queryset = self.queryset.filter(customer_id=request.custom_user['id'])
        serializer = TransactionResponseDetailSerializer(queryset, many=True)
        data = copy.deepcopy(serializer.data)
        for i in data:
            if i['readyAt']: 
                date =  datetime.datetime.strptime(i['readyAt'],'%Y-%m-%dT%H:%M:%S%z')
                i['readyAt']=date.strftime("%d %B %Y")
        return Response(data,status=200)
    
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
        readyAt = ''
        # tr_detail = []
        for index,i in enumerate(products):
            if index == 0: 
                seller = Product.objects.get(pk=i['product_id']).seller.id
                readyAt = i['readyAt'].date()
            if readyAt.date() < i['readyAt'].date(): readyAt = i['readyAt']
            # detail = {}
            # product = i['product_id']
            # product_price = i['product_price']
            # quantity = i['quantity']
            # detail['product_id'] = product
            # detail['product_price'] = product_price
            # detail['quantity'] = quantity
            # tr_detail.append(copy.deepcopy(detail))
        transaction = Transaction.objects.create(customer_id = customer, seller_id = seller, address = address,readyAt=readyAt)
        serz = TransactionSerializer(transaction,many=False)
        id_transaction = serz.data['id']
        for i in products:
            i.pop('readyAt')
            transaction_detail = TransactionDetail.objects.create(transaction_id=id_transaction,**i)
        transaction_status = TransactionStatus.objects.create(transaction_id=id_transaction, masterStatus_id=1)
        payment = Payment.objects.create(transaction_id=id_transaction, paymentType_id=1, paymentMethod_id=payment_method, nominal=nominal)
        send_notification('NO REPLY - ALREADY PAY DOWN PAYMENT - [NAMEAPPS]' ,id_transaction, 'already_pay_dp')
        send_notification('NO REPLY - TO BE CONFIRM - [NAMEAPPS]',id_transaction, 'product_to_be_confirm')
        return Response(status=200)
    
    @action(detail=False, methods=['get'], url_path='checking-seller-confirmation')
    @transaction.atomic
    def job_checking_seller_confirmation(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=1)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 1]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=1).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered.date() + datetime.timedelta(days=3) < datetime.datetime.now().date():
                send_notification('NO REPLY - TIME LIMIT CONFIRMATION - [NAMEAPPS]' ,i.transaction.id, 'time_limit_confirmation')
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus_id=9)
        return Response(status=200)
    
    # create job that cancel the order because the seller pre order is time limit
    @transaction.atomic
    @action(detail=False, methods=['get'], url_path='checking-time-limit-seller-preorder')
    def job_checking_time_limit_seller_preorder(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=2)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 2]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=2).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.transaction.readyAt.date() + datetime.timedelta(days=1) < datetime.datetime.now().date():
                send_notification('NO REPLY - TIME LIMIT PRE ORDER - [NAMEAPPS]' ,i.transaction.id, 'time_limit_preorder')
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus_id=10)
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
                send_notification('NO REPLY - TIME LIMIT FULL PAYMENT - [NAMEAPPS]' ,i.transaction.id, 'time_limit_full_payment')
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus_id=11)
        return Response(status=200)
    
    @action(detail=False, methods=['get'], url_path='checking-due-date-sending-product')
    @transaction.atomic
    def job_checking_due_date_sending_product(self,request):
        list_tr_id = [i.transaction.id for i in TransactionStatus.objects.filter(masterStatus_id=5)]
        transaction_status_exclude = [i.id for i in TransactionStatus.objects.filter(transaction__id__in=list_tr_id) if i.masterStatus.id > 5]
        transaction_status_to_check = TransactionStatus.objects.filter(masterStatus_id=5).exclude(id__in = transaction_status_exclude)
        for i in transaction_status_to_check:
            if i.dateOrdered.date() + datetime.timedelta(days=3) < datetime.datetime.now().date():
                send_notification('NO REPLY - TIME LIMIT SEND PRODUCT - [NAMEAPPS]' ,i.transaction.id, 'time_limit_send_product')
                TransactionStatus.objects.create(transaction_id=i.transaction.id, masterStatus_id=12)
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
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='full-payment')
    def fullPayment(self, request, *args, **kwargs):
        validate_input(request.data,['transaction','paymentMethod','nominal'])
        transaction = request.data['transaction']
        paymentMethod = request.data['paymentMethod']
        nominal = request.data['nominal']
        payment = Payment.objects.create(transaction_id=transaction,paymentMethod_id=paymentMethod,nominal=nominal,paymentType_id=2)
        transaction_status = TransactionStatus.objects.create(transaction_id=transaction,masterStatus_id=4)
        transaction_query = self.queryset.get(pk=transaction)
        serz = TransactionResponseDetailSerializer(transaction_query, many=False)
        send_notification('NO REPLY - NEED TO SEND PRODUCTS - [NAMEAPPS]',transaction,'product_need_to_send')
        send_notification('NO REPLY - ALREADY PAY FULL PAYMENT - [NAMEAPPS]',transaction,'already_pay_fp')
        return Response(serz.data,status=200)
    
    @transaction.atomic
    @action(detail=False, methods=['post'], url_path='deliver-product')
    def deliverProduct(self, request, *args, **kwargs):
        validate_input(request.data,['noResi','courierName','transaction'])
        transaction = Transaction.objects.get(pk=request.data['transaction'])
        transaction.noResi = request.data['noResi']
        transaction.courierName = request.data['courierName']
        transaction.save()
        transactionStatus = TransactionStatus.objects.create(transaction_id = request.data['transaction'], masterStatus_id = 5)
        send_notification('NO REPLY - SENDING PRODUCTS - [NAMEAPPS]',request.data['transaction'],'sending_product')
        serz = TransactionResponseDetailSerializer(transaction,many=False)
        return Response(serz.data,status=200)

    @action(detail=False, methods=['post'], url_path='seller-confirm-delivered')
    def sellerConfirmDelivered(self, request, *args, **kwargs):
        validate_input(request.data,['transaction'])
        TransactionStatus.objects.create(transaction_id = request.data['transaction'], masterStatus_id = 6)
        return Response(status=200)
    
    @action(detail=False, methods=['post'], url_path='customer-confirm-delivered')
    def customerConfirmDelivered(self, request, *args, **kwargs):
        validate_input(request.data,['transaction'])
        TransactionStatus.objects.create(transaction_id = request.data['transaction'], masterStatus_id = 7)
        return Response(status=200)
        

