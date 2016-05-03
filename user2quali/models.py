from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from quali.models import quali
# Create your models here.
class user2quali(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    quali = models.OneToOneField(quali)
    date = models.DateField(timezone.now)
