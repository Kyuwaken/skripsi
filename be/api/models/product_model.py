from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class Product(SoftDeleteModel):
    name = models.CharField(max_length=255)
    category = auto_prefetch.ForeignKey(
        'Category', on_delete=models.CASCADE, null=True, db_constraint=False)
    seller = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False)
    price = models.CharField(max_length=255)
    preorderTime = models.CharField(max_length=255)
    prodcutDescription = models.TextField()
    productPhoto = models.CharField(max_length=255, null=True, blank=True)
    