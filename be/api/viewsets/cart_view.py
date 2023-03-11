from rest_framework import viewsets
from ..serializers import CartResponseSerializer
from ..models import Cart
from rest_framework.permissions import IsAuthenticated
from api.utils import custom_viewset

class CartViewSet(custom_viewset.CustomModelWithHistoryViewSet):
    serializer_class = CartResponseSerializer
    queryset = Cart.objects.all()
    permission_classes = (IsAuthenticated,)