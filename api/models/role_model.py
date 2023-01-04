from django.db import models
from django_softdelete.models import SoftDeleteModel

class Role(SoftDeleteModel):
    name = models.CharField(max_length=255)