from django.db import models
from django_softdelete.models import SoftDeleteModel

class Courier(SoftDeleteModel):
    name = models.CharField(max_length=255)