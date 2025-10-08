from django.forms import ModelForm
from main import models
from django.utils.html import strip_tags

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        fields = ["name", "price", "stock", "description", "thumbnail", "category", "is_featured", "player", "club"]

    def clean_name(self):
        name = self.cleaned_data["name"]
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
    
    def clean_player(self):
        player = self.cleaned_data["player"]
        return strip_tags(player)
        
    def clean_club(self):
        club = self.cleaned_data["club"]
        return strip_tags(club)
