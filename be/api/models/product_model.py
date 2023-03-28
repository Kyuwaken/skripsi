from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel

class Product(TimestampModel, UserTrackModel, SoftDeleteModel):
    name = models.CharField(max_length=255)
    category = auto_prefetch.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True, db_constraint=False)
    seller = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False)
    price = models.IntegerField(default=0)
    preorderTime = models.IntegerField(null=True,blank=True)
    productDescription = models.TextField()
    def __str__(self) -> str:
        return self.name
    