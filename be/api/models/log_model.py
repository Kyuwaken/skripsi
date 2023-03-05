from django.db import models
from django.contrib.contenttypes.models import ContentType


class Log(models.Model):
    CREATED = 0
    UPDATED = 1
    DELETED = 2
    ACTION_TYPE = (
        (0, 'CREATED'),
        (1, 'UPDATED'),
        (2, 'DELETED')
    )

    user = models.CharField(max_length=255, blank=True, null=True)
    object_id = models.CharField(max_length=255)
    serialized_data = models.TextField()
    serialized_data.parse_json = True
    object_repr = models.TextField()
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    action_time = models.DateTimeField(auto_now=True)
    action = models.IntegerField(choices=ACTION_TYPE)

    class Meta:
        ordering = ['-action_time']

    @staticmethod
    def get_content_type(instance):
        content_type = ContentType.objects.get(
            app_label=instance._meta.app_label,
            model=str(instance.__class__.__name__).lower()
        )
        return content_type

    @staticmethod
    def get_content_class_type(model):
        content_type = ContentType.objects.get(
            app_label=model._meta.app_label,
            model=str(model.__name__).lower()
        )
        return content_type
