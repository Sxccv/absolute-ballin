from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('equipment', 'Equipment'),
        ('supplement', 'Supplement'),
        ('misc', 'Misc'),
        ('merch', 'Merch'),
        ('player', 'Player'),
    ]


    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price =  models.PositiveIntegerField(default=0)
    stock =  models.IntegerField(default=0)
    description = models.TextField()
    thumbnail = models.URLField(blank=True, default='https://cdn.nba.com/manage/2021/08/michael-jordan-looks.jpg')
    category = models.CharField(max_length=25, choices=CATEGORY_CHOICES, default='misc')
    is_featured = models.BooleanField(default=False,blank=True,null=True)
    player = models.CharField(max_length=255,blank=True,null=True)
    club = models.CharField(max_length=255,blank=True,null=True)