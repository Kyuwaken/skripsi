from rest_framework import viewsets
from ..serializers import TransactionSerializer,TransactionResponseSerializer
from ..models import Transaction, Product, User, TransactionDetail, Payment, TransactionStatus
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response
import copy

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
        tr_detail = []
        for i in products:
            if i == 0: seller = Product.objects.get(pk=i['product_id']).seller.id
            detail = {}
            product = i['product_id']
            product_price = i['product_price']
            quantity = i['quantity']
            detail['product'] = product
            detail['product_price'] = product_price
            detail['quantity'] = quantity
            tr_detail.append(copy.deepcopy(detail))
        
            
        
        return super().create(request, *args, **kwargs)