from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class UserDetail(SoftDeleteModel):
    NIK = models.CharField(max_length=255)
    userId = auto_prefetch.ForeignKey(
        'User', on_delete=models.CASCADE, null=True, db_constraint=False)
    countryId = auto_prefetch.ForeignKey(
        'Country', on_delete=models.CASCADE, null=True, db_constraint=False)