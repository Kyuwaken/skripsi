from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel

class ProductReview(TimestampModel, UserTrackModel, SoftDeleteModel):
    customer = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False)
    product = auto_prefetch.ForeignKey(
        'Product', on_delete=models.CASCADE, null=True, db_constraint=False)
    rating = models.CharField(max_length=255)
    review = models.TextField(null=True, blank=True)
    