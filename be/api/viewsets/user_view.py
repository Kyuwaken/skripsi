from rest_framework import viewsets
from ..serializers import UserSerializer, UserResponseSerializer
from ..models import User
from api.permissions import IsAuthenticated
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException,ValidationException
from rest_framework.response import Response
from api.permissions import IsSignUp
class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (IsSignUp,)

    def list(self, request):
        queryset = self.queryset.select_related('role','country')
        serializer = UserResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            user =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("User")
        serializer = UserResponseSerializer(user, many=False)
        return Response(serializer.data,status=200)
    
    def create(self, request, *args, **kwargs):
        all_username = [i.username for i in self.queryset]
        if request.data['username'] in all_username:
            raise ValidationException('Username already exists')
        return super().create(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        all_username = [i.username for i in self.queryset if i.id != kwargs]
        if request.data['username'] in all_username:
            raise ValidationException('Username already exists')
        return super().update(request, *args, **kwargs)
    
