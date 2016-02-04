from django.db import models
from quali import models as quali_models
from orgs import models as org_models
# Create your models here.
class Name(models.Model):
    name_text = (models.CharField(max_length=255))
    vorname_text = (models.CharField(max_length=255))

class Adress(models.Model):
    street_text = (models.CharField(max_length=255))
    number_int = (models.IntegerField)
    city_text = (models.CharField(max_length=255))
    zip_int = (models.CharField(default=3763))

class UserQuali(models.Model):
    quali_text = (models.ForeignKey(quali_models.Quali.quali_text))
    quali_date = (models.DateField)

class Member(models.Model):
    org_member_text = (models.ForeignKey(org_models.Organisations.org_name_text))