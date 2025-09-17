from django.db import models
import uuid


# Create your models here.

class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    price =  models.PositiveIntegerField(default=0)
    stock =  models.PositiveIntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField()
    category = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False,blank=True,null=True)
    player = models.CharField(max_length=255,blank=True,null=True)
    club = models.CharField(max_length=255,blank=True,null=True)
    