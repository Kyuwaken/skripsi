from rest_framework import viewsets
from ..serializers import UserSerializer, UserResponseSerializer
from ..models import User
from rest_framework.permissions import IsAuthenticated
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('role','country')
        serializer = UserResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            user =  self.queryset.get(pk=kwargs['pk']).select_related('role','country')
        except ObjectDoesNotExist:
            raise NotFoundException("User")
        serializer = UserResponseSerializer(user, many=False)
        return Response(serializer.data,status=200)