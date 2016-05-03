from django.db import models
from django.utils import timezone
from user.models import User

def eventTime():
    return timezone.now() + timezone.timedelta(hours=2)

# Create your models here.
class events(models.Model):
    name = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)
    start = models.DateTimeField(timezone.now)
    end = models.DateTimeField(eventTime())
    is_course = models.BooleanField(default=True)
    is_training = models.BooleanField(default=False)


