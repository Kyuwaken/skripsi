from rest_framework import viewsets
from ..serializers import FavouriteSerializer, FavouriteResponseSerializer
from ..models import Favourite
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

class FavouriteViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = FavouriteSerializer
    queryset = Favourite.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('user','product')
        serializer = FavouriteResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            favourite =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Favourite")
        serializer = FavouriteResponseSerializer(favourite, many=False)
        return Response(serializer.data,status=200)