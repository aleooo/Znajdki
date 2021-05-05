from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User

from . import views
from .models import Rzeczy, Mapa, Kategoria


class PoszukiwaniaTests(TestCase):

    def test_login_adminsite(self):
        password = 'aletojuzbylo'
        admin = User.objects.create_user('aleo', 'medda@test.com', password)
        self.c = Client()
        self.c.login(username=admin.username, password=password)

    def test_url(self):
        url = reverse('poszukiwania:start')
        self.assertEqual(resolve(url).func, views.start)

    def test_view(self):
        client = Client()
        response = client.get(reverse('poszukiwania:start'))
        self.assertEqual(response.status_code, 200)

    def test_home_page(self):
        request = HttpRequest()
        response = views.start(request)
        self.assertEqual(response.status_code, 200)
        expected_html = render_to_string('main/lista.html')
        self.assertEqual(response.content.decode(), expected_html)

    def test_register(self):
        request = HttpRequest()
        request.method = 'POST'
        response = views.register(request)
        expected_html = render_to_string('main/register.html')
        # self.assertEqual(response.content.decode(), expected_html)

    def test_model_orm(self):
        password = 'aletojuzbylo'
        admin = User.objects.create_user('aleo', 'medda@test.com', password)

        geolokalizacja = {'type': 'Point', 'coordinates': [21.919698715209964, 52.00461918344298]}
        Mapa.objects.create(geolokalizacja=geolokalizacja)
        mapa = Mapa.objects.first()
        self.assertEqual(mapa.geolokalizacja, geolokalizacja)

        Kategoria.objects.create(title='monety', slug='monety')
        kategoria = Kategoria.objects.first()
        self.assertEqual(kategoria.title, 'monety')

        Rzeczy.objects.create(user=admin,
                              location=mapa,
                              kategoria=kategoria,
                              title='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='często spotykana moneta')
        self.rzecz = Rzeczy.objects.first()
        self.assertEqual(self.rzecz.title, 'Boratynka')













# def test_rzeczy_list(self):
#     client = Client()
#
#     request = HttpRequest
#     response = views.rzeczy_list(client.request)
#     print(response)


