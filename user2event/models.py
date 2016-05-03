from django.db import models
from events.models import events
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class user2event(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    event = models.OneToOneField(events)
    date = models.DateField(timezone.now)
