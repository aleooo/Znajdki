from django.test import TestCase
from django.urls import reverse, resolve
from .views import start
from .models import Rzeczy, Mapa

class PoszukiwaniaTests(TestCase):

    def test_url(self):
        url = reverse('poszukiwania:start')
        print(resolve(url))
        self.assertEqual(resolve(url).url_name, 'start')

    def test_map(self):
        Mapa.objects.create(geolokalizacja={'type': 'Point', 'coordinates': [21.920471191406254, 52.00424932154731]})
        a = Mapa.objects.filter(geolokalizacja={'type': 'Point', 'coordinates': [21.920471191406254, 52.00424932154731]})
        print(a.geolokalizacja)
    # def test_object(self):
    #     Rzeczy.objects.create(title='Grosz Testu', )


# {'type': 'Point', 'coordinates': [21.920471191406254, 52.00424932154731]}
# < Mapa: Mapa object(13) >
