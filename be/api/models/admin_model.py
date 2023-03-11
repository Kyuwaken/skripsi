# from django_softdelete.models import SoftDeleteModel
# from api.models.abstract_model import TimestampModel, UserTrackModel
# from django.db import models

# class Admin(TimestampModel, UserTrackModel, SoftDeleteModel):
#     username = models.CharField(max_length=255, unique=True)
#     password = models.CharField(max_length=255, default='admin123')
#     def __str__(self) -> str:
#         return self.name