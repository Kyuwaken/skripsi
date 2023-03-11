from rest_framework import viewsets
from ..serializers import FavouriteResponseSerializer
from ..models import Favourite
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class FavouriteViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = FavouriteResponseSerializer
    queryset = Favourite.objects.all()
    permission_classes = (IsAuthenticated,)