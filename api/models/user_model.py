from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class User(SoftDeleteModel):
    name = models.CharField(max_length=255)
    roleId = auto_prefetch.ForeignKey(
        'Role', on_delete=models.CASCADE, null=True, db_constraint=False)
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)