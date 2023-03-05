from django.db import models
import auto_prefetch
from django_softdelete.models import SoftDeleteModel

class User(SoftDeleteModel):
    name = models.CharField(max_length=255, default='')
    role = auto_prefetch.ForeignKey(
        'Role', on_delete=models.CASCADE, null=True, db_constraint=False)
    phone = models.CharField(max_length=255, default='')
    email = models.CharField(max_length=255,default='')
    password = models.CharField(max_length=255,default='admin123')
    address = models.TextField(default='')

    def __str__(self) -> str:
        return self.name