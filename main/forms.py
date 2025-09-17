from django.forms import ModelForm
from main import models

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ["name", "price", "stock", "description", "thumbnail", "category", "is_featured", "player", "club"]
