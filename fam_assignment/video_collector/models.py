from django.db import models
from datetime import datetime
from django.contrib.postgres.fields import ArrayField

class Video(models.Model):

    title = models.CharField(max_length=100)
    description = models.CharField(max_length=1000)
    published_at = models.DateTimeField()
    urls = ArrayField(
        models.URLField(max_length=100, blank=True),
        blank = True,
        null = True,
    )
    channelTitle = models.CharField(max_length=100)

    def __str__(self):
        return self.title