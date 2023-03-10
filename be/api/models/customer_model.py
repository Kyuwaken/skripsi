from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel
from django.db import models

class Customer(TimestampModel, UserTrackModel, SoftDeleteModel):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, default='customer123')
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255, default='')
    address = models.TextField(default='')
    def __str__(self) -> str:
        return self.name