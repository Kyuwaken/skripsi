import auto_prefetch
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel
from django.db import models
from cryptography.fernet import Fernet
from api.utils.pycrypto import encrypt_data
from django.conf import settings


class User(TimestampModel, UserTrackModel, SoftDeleteModel):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    role = auto_prefetch.ForeignKey(
        'Role', on_delete=models.CASCADE, null=True, db_constraint=False)
    phone = models.CharField(max_length=255, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    country = auto_prefetch.ForeignKey(
        'Country', on_delete=models.CASCADE, null=True, db_constraint=False)
    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        self.password = encrypt_data(self.password)
        return super().save(*args,**kwargs)