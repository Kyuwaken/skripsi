from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel
from django.db import models

class Customer(TimestampModel, UserTrackModel, SoftDeleteModel):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='admin123')
    address = models.TextField(default='')
    def __str__(self) -> str:
        return self.name