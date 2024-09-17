from django.forms import ModelForm
from main.models import ShopEntry

class ShopEntryForm(ModelForm):
    class Meta:
        model = ShopEntry 
        fields = ["product_name", "price", "quantity", "location", "description"]