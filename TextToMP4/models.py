from django.db import models


class TextToMP4Requests(models.Model):
    text = models.CharField(max_length=120)
    duration = models.IntegerField()
    rect_size = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
