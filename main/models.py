from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=255)
    price =  models.PositiveIntegerField(default=0)
    stock =  models.IntegerField(default=0)
    description = models.TextField(max_length=200)
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False,blank=True,null=True)
    player = models.CharField(max_length=255,blank=True,null=True)
    club = models.CharField(max_length=255,blank=True,null=True)