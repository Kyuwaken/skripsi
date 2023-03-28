from rest_framework import viewsets
from ..serializers import CategorySerializer
from ..models import Category
from api.permissions import IsAuthenticated
from api.utils import custom_viewset

class CategoryViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    permission_classes = (IsAuthenticated,)