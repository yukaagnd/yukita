from django.db import models
import uuid 

class ShopEntry(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField()
