from django.test import  TestCase,Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from . import views
from .models import Rzeczy, Mapa, Kategoria


class PoszukiwaniaTests(TestCase):

    def setUp(self):
        self.geolokalizacja = {'type': 'Point', 'coordinates': [21.919698715209964, 52.00461918344298]}
        self.password = 'aletojuzbylo'
        kategoria = Kategoria.objects.create(title='monety', slug='monety')
        mapa = Mapa.objects.create(geolokalizacja=self.geolokalizacja)

        self.user = User.objects.create_user('aleo', 'medda@test.com', self.password)
        Rzeczy.objects.create(user=self.user,
                              location=mapa,
                              kategoria=kategoria,
                              title='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='często spotykana moneta',
                              image=SimpleUploadedFile(name='12.jpg', content=open('/home/aleo/projects/znajdki/znajdki/poszukiwania/static/css/12.jpg', 'rb').read(), content_type='image/jpeg'))

    def test_login_adminsite(self):
        self.c = Client()
        self.c.login(username=self.user.username, password=self.password)

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
        mapa = Mapa.objects.first()
        self.assertEqual(mapa.geolokalizacja, self.geolokalizacja)
        kategoria = Kategoria.objects.first()
        self.assertEqual(kategoria.title, 'monety')
        rzecz = Rzeczy.objects.first()
        self.assertEqual(rzecz.title, 'Boratynka')

    def test_view_rzeczy_list(self):
        request = HttpRequest()
        request.user = self.user
        response = views.rzeczy_list(request)

        print(response.content.decode())











# def test_rzeczy_list(self):
#     client = Client()
#
#     request = HttpRequest
#     response = views.rzeczy_list(client.request)
#     print(response)


