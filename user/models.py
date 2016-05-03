from django.db import models
from django.contrib.auth.models import User
from quali.models import quali
from orgs.models import orgs
from django.utils import timezone

# Create your models here.
class employee(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    street_text = models.CharField(max_length=255)
    number_int = models.IntegerField(default=10)
    city_text = models.CharField(max_length=255)
    zip_int = models.IntegerField(default=3673)
    phone = models.IntegerField()
    mobile = models.IntegerField()
    mail = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    org_member = models.ManyToManyField(orgs)
