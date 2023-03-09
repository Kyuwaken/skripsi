from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel

class Transaction(TimestampModel, UserTrackModel, SoftDeleteModel):
    seller = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False, related_name='seller')
    customer = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False, related_name='customer')
    dateOrdered = models.DateTimeField(auto_now_add=True)
    # statusTransaksi = models.CharField(max_length=255)
    noResi = models.TextField()
    courierName = models.CharField(max_length=255)
    courierPrice = models.CharField(max_length=255)
    