from django.db import models
import uuid 

class ShopEntry(models.Model):
    name = models.CharField(max_length=255)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    note = models.TextField()

    @property
    def is_buy_wholesale(self):
        return self.quantity > 10
