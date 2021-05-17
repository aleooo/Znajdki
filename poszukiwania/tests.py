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
        self.password = 'aletojuzbylo'
        kategoria = Kategoria.objects.create(title='monety', slug='monety')
        kategoria1 = Kategoria.objects.create(title='guziki', slug='guziki')
        mapa = Mapa.objects.create(description='punkt')
        mapa1 = Mapa.objects.create(description='punkt1')
        self.user = User.objects.create_user('aleo', 'medda@test.com', self.password)
        Rzeczy.objects.create(user=self.user,
                              location=mapa,
                              kategoria=kategoria,
                              title='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='często spotykana moneta',
                              image=SimpleUploadedFile(name='12.jpg', content=open('/home/aleo/projects/znajdki/znajdki/poszukiwania/static/css/12.jpg', 'rb').read(), content_type='image/jpeg'))
        Rzeczy.objects.create(user=self.user,
                              location=mapa1,
                              kategoria=kategoria1,
                              title='wz19',
                              slug='wz19',
                              year=1919,
                              text='rzadko spotykany guzik',
                              image=SimpleUploadedFile(name='12.jpg', content=open(
                                  '/home/aleo/projects/znajdki/znajdki/poszukiwania/static/css/wz19.jpg', 'rb').read(),
                                                       content_type='image/jpeg'))

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
        mapa = Mapa.objects.count()
        self.assertEqual(mapa, 2)
        kategoria = Kategoria.objects.first()
        self.assertEqual(kategoria.title, 'monety')
        rzecz = Rzeczy.objects.first()
        self.assertEqual(rzecz.title, 'Boratynka')

    def test_view_rzeczy_list(self):
        request = HttpRequest()
        request.user = self.user
        response = views.rzeczy_list(request)
        self.assertIn('Boratynka', response.content.decode())

    def test_view_rzeczy_list_with_category(self):
        kategoria = Kategoria.objects.first()
        request = HttpRequest()
        request.user = self.user
        response = views.rzeczy_list(request, kategoria.slug)
        self.assertIn('Boratynka', response.content.decode())













