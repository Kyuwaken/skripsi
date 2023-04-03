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
    
    def get_created_by(self, obj):
        if obj.created_by:
            return obj.created_by.display_name
        return None

    def get_updated_by(self, obj):
        if obj.updated_by:
            return obj.updated_by.display_name
        return None