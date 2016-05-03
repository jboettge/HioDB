from django.db import models

# Create your models here.
class orgs(models.Model):
    name = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    street_number = models.IntegerField()
    zip = models.IntegerField(default=3763)
    city = models.CharField(max_length=50)
    county = models.CharField(max_length=2)
    country = models.CharField(max_length=2)
    tel = models.IntegerField()
    mail = models.CharField(max_length=255)
    web = models.CharField(max_length=255)