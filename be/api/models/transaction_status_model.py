from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel

class TransactionStatus(TimestampModel, UserTrackModel, SoftDeleteModel):
    transaction = auto_prefetch.ForeignKey(
        'Transaction', on_delete=models.CASCADE, null=True, db_constraint=False, related_name='transaction_status')
    masterStatus = auto_prefetch.ForeignKey(
        'MasterStatus', on_delete=models.CASCADE, null=True, db_constraint=False)
    dateOrdered = models.DateTimeField(auto_now_add=True)
    notes = models.TextField(null=True, blank=True)
    