from rest_framework import viewsets
from ..serializers import ProductReviewSerializer, ProductReviewResponseSerializer
from ..models import ProductReview
from api.permissions import IsAuthenticated
from api.utils import custom_viewset
from django.db.models.base import ObjectDoesNotExist
from api.exceptions import NotAuthorizedException,NotFoundException
from rest_framework.response import Response
from rest_framework.decorators import action
from api.utils.validation_input import validate_integer, validate_input
from django.db import transaction

class ProductReviewViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = ProductReviewSerializer
    queryset = ProductReview.objects.all()
    permission_classes = (IsAuthenticated,)

    def list(self, request):
        queryset = self.queryset.select_related('user','product')
        serializer = ProductReviewResponseSerializer(queryset, many=True)
        return Response(serializer.data, status=200)
    
    def retrieve(self, request, *args, **kwargs):
        try:
            product_review =  self.queryset.get(pk=kwargs['pk'])
        except ObjectDoesNotExist:
            raise NotFoundException("Product Review")
        serializer = ProductReviewResponseSerializer(product_review, many=False)
        return Response(serializer.data,status=200)
    
    @action(detail=False, methods=['post'], url_path='seller')
    def get_by_seller_id(self, request, *args, **kwargs):
        validate_input(request.data,['id'])
        queryset = self.queryset.filter(seller_id=request.data['id'], is_deleted=False)
        serializer = ProductReviewResponseSerializer(queryset,many=True)
        return Response(serializer.data,status=200)