from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel
import auto_prefetch
from django.db import models

class Seller(TimestampModel, UserTrackModel, SoftDeleteModel):
    name = models.CharField(max_length=255, default='')
    phone = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='admin123')
    address = models.TextField(default='')
    country = auto_prefetch.ForeignKey(
        'Country', on_delete=models.CASCADE, null=True, db_constraint=False)
    def __str__(self) -> str:
        return self.name