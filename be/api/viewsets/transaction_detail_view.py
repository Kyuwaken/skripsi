from rest_framework import viewsets
from ..serializers import TransactionDetailSerializer,TransactionDetailResponseSerializer
from ..models import TransactionDetail
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

class TransactionDetailViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = TransactionDetailResponseSerializer
    queryset = TransactionDetail.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('transaction','product')
        serializer = TransactionDetailResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            transaction_detail =  self.queryset.get(pk=kwargs['pk']).select_related('transaction','product')
        except ObjectDoesNotExist:
            raise NotFoundException("Transaction Detail")
        serializer = TransactionDetailResponseSerializer(transaction_detail, many=False)
        return Response(serializer.data,status=200)