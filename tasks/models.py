from django.db import models
from django.utils import timezone
# Create your models here.

class tasks(models.Model):
    name = models.CharField(max_length=50)
    descr = models.CharField(max_length=255)
    start = models.DateTimeField(timezone.now)
    end = models.DateTimeField(timezone.now)