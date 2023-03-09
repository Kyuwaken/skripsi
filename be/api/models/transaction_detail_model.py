from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel

class TransactionDetail(TimestampModel, UserTrackModel, SoftDeleteModel):
    transaction = auto_prefetch.ForeignKey(
        'Transaction', on_delete=models.CASCADE, null=True, db_constraint=False)
    product = auto_prefetch.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True, db_constraint=False)
    quantity = models.IntegerField()
    productPrice = models.CharField(max_length=255)