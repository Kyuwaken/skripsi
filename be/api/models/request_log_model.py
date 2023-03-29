from django.db import models


class RequestLog(models.Model):
    user = models.CharField(max_length=255,null=True)
    url = models.TextField()
    method = models.CharField(max_length=255)
    header = models.TextField()
    header.parse_json = True
    parameter = models.TextField()
    parameter.parse_json = True
    body = models.TextField()
    body.parse_json = True
    action_time = models.DateTimeField(auto_now=True)
    response_code = models.CharField(max_length=255)
    role = models.CharField(max_length=255, null=True)

    class Meta:
        ordering = ['-action_time']
