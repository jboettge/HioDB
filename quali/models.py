from django.db import models
from django.utils import timezone
# Create your models here.
class quali(models.Model):
    name = models.CharField(max_length=50)
    descr = models.CharField(max_length=255)
    date = models.DateField(timezone.now)
