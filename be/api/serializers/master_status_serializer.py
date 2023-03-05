from rest_framework import serializers
from ..models import MasterStatus


class MasterStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = MasterStatus
        fields = '__all__'