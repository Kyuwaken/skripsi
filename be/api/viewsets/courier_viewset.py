from rest_framework import viewsets
from ..serializers import CourierSerializer
from ..models import Courier
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class CourierViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = CourierSerializer
    queryset = Courier.objects.all()
    permission_classes = (IsAuthenticated,)