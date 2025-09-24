from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price =  models.PositiveIntegerField(default=0)
    stock =  models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False,blank=True,null=True)
    player = models.CharField(max_length=255,blank=True,null=True)
    club = models.CharField(max_length=255,blank=True,null=True)