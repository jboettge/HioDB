from django.db import models

# Create your models here.
class Quali(models.Model):
    quali_text = (models.CharField(max_length=255))
    quali_date = (models.DateField())