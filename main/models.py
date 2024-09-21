from django.db import models
import uuid 
from django.contrib.auth.models import User

class ShopEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    product_name = models.CharField(max_length=255)
    price = models.IntegerField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    description = models.TextField()
