from django.db import models


class Task(models.Model):
    DoesNotExist = None
    objects = None
    body = models.CharField(max_length=255)

    def __str__(self):
        return self.body
