from rest_framework import viewsets
from ..serializers import TransactionSerializer,TransactionResponseSerializer
from ..models import Transaction
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

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