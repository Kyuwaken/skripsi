from rest_framework import viewsets
from ..serializers import PaymentSerializer, PaymentResponseSerializer
from ..models import Payment
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

class PaymentViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('transaction','paymentType','paymentMethod')
        serializer = PaymentResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            payment =  self.queryset.get(pk=kwargs['pk']).select_related('transaction','paymentType','paymentMethod')
        except ObjectDoesNotExist:
            raise NotFoundException("Payment")
        serializer = PaymentResponseSerializer(payment, many=False)
        return Response(serializer.data,status=200)