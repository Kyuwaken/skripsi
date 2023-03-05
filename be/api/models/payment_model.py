from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class Payment(SoftDeleteModel):
    transaction = auto_prefetch.ForeignKey(
        'Transaction', on_delete=models.CASCADE, null=True, db_constraint=False)
    paymentType = auto_prefetch.ForeignKey(
        'PaymentType', on_delete=models.CASCADE, null=True, db_constraint=False)
    paymentMethod = auto_prefetch.ForeignKey(
        'PaymentMethod', on_delete=models.CASCADE, null=True, db_constraint=False)
    paymentStatus = models.BooleanField()
    