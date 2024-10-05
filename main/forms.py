from django.forms import ModelForm
from main.models import ShopEntry
from django.utils.html import strip_tags

class ShopEntryForm(ModelForm):
    class Meta:
        model = ShopEntry 
        fields = ["product_name", "price", "quantity", "location", "description"]
    
    def clean_product_name(self):
        product_name = self.cleaned_data["product_name"]
        return strip_tags(product_name)

    def clean_location(self):
        location = self.cleaned_data["location"]
        return strip_tags(location)
    
    def clean_description(self):
        description = self.cleaned_data["description"]
        return strip_tags(description)
