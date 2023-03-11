from rest_framework import viewsets
from ..serializers import ProductReviewResponseSerializer
from ..models import ProductReview
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class ProductReviewViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = ProductReviewResponseSerializer
    queryset = ProductReview.objects.all()
    permission_classes = (IsAuthenticated,)