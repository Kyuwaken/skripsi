from rest_framework import viewsets
from ..serializers import CourierSerializer
from ..models import Courier
from rest_framework.permissions import IsAuthenticated

class CourierViewSet(viewsets.ModelViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()
    permission_classes = (IsAuthenticated,)