from django.db import models

# Create your models here.
class Inventory(models.Model):
    qty = models.SmallIntegerField()
    image = models.CharField(max_length=60)
    item = models.CharField(max_length=60)
    category = models.CharField(max_length=60)
    expiry = models.DateField()