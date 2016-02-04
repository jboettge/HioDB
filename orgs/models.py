from django.db import models

# Create your models here.
class Organisations(models.Model):
    org_name_text = (models.CharField(max_length=255))
    org_street_addr_text = (models.CharField(max_length=255))
    org_zip_int = (models.IntegerField)
    org_city_addr_text = (models.CharField(max_length=255))
    org_tel_int = (models.IntegerField)