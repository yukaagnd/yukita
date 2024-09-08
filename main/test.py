from django.test import TestCase, Client
from django.utils import timezone
from .models import ShopEntry

class mainTest(TestCase):
    def test_main_url_is_exist(self):
        response = Client().get('')
        self.assertEqual(response.status_code, 200)

    def test_main_using_main_template(self):
        response = Client().get('')
        self.assertTemplateUsed(response, 'main.html')

    def test_nonexistent_page(self):
        response = Client().get('/skibidi/')
        self.assertEqual(response.status_code, 404)

    def test_is_avaible(self):
        item = ShopEntry.objects.create(
            name = "Adidas Samba",
            price = 2200000,
            description = "Lace up in legendary style. These adidas Samba LT shoes bring a retro sport vibe to your everyday style. Once an indoor football trainer, now a streetwear staple, this version makes a striking statement with an oversized football-inspired tongue. Crafted in premium leather with a sleek nubuck toe, they lend a sophisticated edge to everything from denim to joggers. A rubber outsole provides lightweight traction and classic good looks.",
            quantity = 15,
            location = "Jakarta", 
        )
        self.assertTrue(item.is_avaible)