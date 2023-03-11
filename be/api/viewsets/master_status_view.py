from rest_framework import viewsets
from ..serializers import MasterStatusSerializer
from ..models import MasterStatus
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class MasterStatusViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = MasterStatusSerializer
    queryset = MasterStatus.objects.all()
    permission_classes = (IsAuthenticated,)