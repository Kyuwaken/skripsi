
import random
from django.db import models
from django.apps import apps
from django.utils import timezone
import auto_prefetch

class TimestampModel(auto_prefetch.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def format_timestamp(self, format):
        created_at = timezone.localtime(self.created_at)
        updated_at = timezone.localtime(self.updated_at)
        self.created_at = created_at.strftime(format)
        self.updated_at = updated_at.strftime(format)

    class Meta:
        abstract = True


class UserTrackModel(auto_prefetch.Model):
    created_by = auto_prefetch.ForeignKey('User', on_delete=models.CASCADE, blank=True, related_name="%(class)s_fk_created", null=True)
    updated_by = auto_prefetch.ForeignKey('User', on_delete=models.CASCADE , null=True, blank=True, related_name="%(class)s_fk_updated")
    class Meta:
        abstract = True