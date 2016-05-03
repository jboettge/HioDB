from django.db import models
from django.contrib.auth.models import User
from tasks.models import tasks
from django.utils import timezone
# Create your models here.

class user2task(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    task = models.OneToOneField(tasks)
    date = models.DateField(timezone.now)