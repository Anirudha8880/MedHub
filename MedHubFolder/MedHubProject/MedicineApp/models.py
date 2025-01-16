from email.policy import default

from django.db import models
from django.forms import IntegerField

# Create your models here

class Medicine(models.Model):
    medicine_name = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
    exp = models.CharField(max_length=100)
    qty = models.IntegerField(default=0)

