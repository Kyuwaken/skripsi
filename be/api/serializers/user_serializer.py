from rest_framework import serializers
# from ..models import Admin,Seller,Customer
from ..models import User
from .role_serializer import RoleSerializer
from .country_serializer import CountrySerializer


# class AdminSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Admin
#         fields = '__all__'

# class SellerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Seller
#         fields = '__all__'

# class CustomerSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Customer
#         fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserResponseSerializer(serializers.ModelSerializer):
    role = RoleSerializer(many=False)
    country = CountrySerializer(many=False)
    class Meta:
        model = User
        fields = '__all__'