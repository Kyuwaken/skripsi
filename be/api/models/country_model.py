from django.db import models
from django_softdelete.models import SoftDeleteModel
from api.models.abstract_model import TimestampModel, UserTrackModel

class Country(TimestampModel, UserTrackModel, SoftDeleteModel):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name