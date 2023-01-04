from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class Cart(SoftDeleteModel):
    userId = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False)
    productId = auto_prefetch.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True, db_constraint=False)
    quantity = models.IntegerField()