from rest_framework import viewsets
from ..serializers import CountrySerializer
from ..models import Country
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class CountryViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()
    permission_classes = (IsAuthenticated,)