from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class TransactionStatus(SoftDeleteModel):
    transaction = auto_prefetch.ForeignKey(
        'Transaction', on_delete=models.CASCADE, null=True, db_constraint=False)
    masterStatus = auto_prefetch.ForeignKey(
        'MasterStatus', on_delete=models.CASCADE, null=True, db_constraint=False)
    dateOrdered = models.DateTimeField(auto_now_add=True)
    notes = models.TextField()
    