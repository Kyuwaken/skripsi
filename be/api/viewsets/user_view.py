from rest_framework import viewsets
from ..serializers import UserSerializer, UserResponseSerializer
from ..models import User, ProductReview
from api.permissions import IsAuthenticated
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException,ValidationException
from rest_framework.response import Response
from api.permissions import IsSignUp
from rest_framework.decorators import action
from api.utils.validation_input import validate_integer, validate_input
import copy
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
        all_username = [i.username for i in self.queryset if i.id != int(kwargs['pk'])]
        if request.data['username'] in all_username:
            raise ValidationException('Username already exists')
        return super().update(request, *args, **kwargs)
    
    @action(detail=False, methods=['post'], url_path='seller')
    def get_by_seller_id(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        queryset = self.queryset.filter(pk=request.data['id'])
        serializer = UserResponseSerializer(queryset, many=False)
        product_review = ProductReview.objects.filter(product__seller_id=request.data['id'])
        count_review = len(product_review)
        rating = sum([i.rating for i in product_review])
        data = copy.deepcopy(serializer.data)
        rates = rating/count_review
        data['rating'] = round(rates,1)
        return Response(data,status=200)

    
