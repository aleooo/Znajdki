from django.test import  TestCase,Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User
from django.core.files.uploadedfile import SimpleUploadedFile

from . import views
from .models import Rzeczy, Mapa, Category


class PoszukiwaniaTestCase(TestCase):

    def setUp(self):
        self.password = 'aletojuzbylo'
        category = Category.objects.create(title='coins', slug='coins')
        category1 = Category.objects.create(title='buttons', slug='buttons')
        map = Mapa.objects.create(description='point')
        map1 = Mapa.objects.create(description='point1')
        self.user = User.objects.create_user('aleo', 'medda@test.com', self.password)
        Rzeczy.objects.create(user=self.user,
                              location=map,
                              category=category,
                              title='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='a frequently found coin',)

        Rzeczy.objects.create(user=self.user,
                              location=map1,
                              category=category1,
                              title='wz19',
                              slug='wz19',
                              year=1919,
                              text='a rarely found button',)



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
        map = Mapa.objects.count()
        self.assertEqual(map, 2)
        category = Category.objects.first()
        self.assertEqual(category.name, 'coins')
        object = Rzeczy.objects.first()
        self.assertEqual(object.name, 'Boratynka')

    def test_view_rzeczy_list(self):
        request = HttpRequest()
        request.user = self.user
        response = views.objects_list(request)
        self.assertIn('Boratynka', response.content.decode())

    def test_view_rzeczy_list_with_category(self):
        category = Category.objects.first()
        request = HttpRequest()
        request.user = self.user
        response = views.objects_list(request, category.slug)
        self.assertIn('Boratynka', response.content.decode())













