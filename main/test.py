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

    def test_is_buy_wholesale(self):
        item = ShopEntry.objects.create(
            name = "Yuka",
            quantity = 15,
            location = "Jakarta", 
            note = "please use bubblewrap"
        )
        self.assertTrue(item.is_buy_wholesale)