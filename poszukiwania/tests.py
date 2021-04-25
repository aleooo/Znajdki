from django.test import TestCase, Client
from django.urls import reverse, resolve
from .views import start
from .models import Rzeczy, Mapa, Kategoria

class PoszukiwaniaTests(TestCase):

    def test_url(self):
        url = reverse('poszukiwania:start')
        print(resolve(url))
        self.assertEqual(resolve(url).func, start)

    def test_view(self):
        client = Client()
        response = client.get(reverse('poszukiwania:start'))
        self.assertEqual(response.status_code, 200)