from django.db import models

class ShopEntry(models.Model):
    name = models.CharField(max_length=255)
    price = models.IntegerField()
    description = models.TextField()
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)

    @property
    def is_avaible(self):
        return self.quantity > 0