from django.test import  TestCase
from django.contrib.auth.models import User

from poszukiwania import views
from poszukiwania.models import Map, Category, Rzeczy

from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import HttpRequest

class ModelsTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(title='coins', slug='coins')
        category1 = Category.objects.create(title='buttons', slug='buttons')
        map1 = Map.objects.create(point='{"lat": 52.01546930699952, "lng": 21.915056009813515}', description='point')
        map2 = Map.objects.create(point='{"lat": 52.01546930199952, "lng": 21.915056009813516}', description='point1')
        self.user = User.objects.create_user('aleo', 'medda@test.com', 'aletojuzbylo')
        self.client_aleo = Client().login(username='aleo', password='aletojuzbylo')
        Rzeczy.objects.create(user=self.user,
                              location=map1,
                              category=category,
                              name='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='a frequently found coin',)

        Rzeczy.objects.create(user=self.user,
                              location=map2,
                              category=category1,
                              name='wz19',
                              slug='wz19',
                              year=1919,
                              text='a rarely found button',)

    def test_model_orm(self):
        map = Map.objects.count()
        self.assertEqual(map, 2)
        category = Category.objects.first()
        self.assertEqual(category.title, 'coins')
        object = Rzeczy.objects.first()
        self.assertEqual(object.name, 'Boratynka')

    def test_view_rzeczy_list(self):
        self.client.login(username='aleo', password='aletojuzbylo')
        response = self.client.get(reverse('poszukiwania:objects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Boratynka')
        # request = HttpRequest()
        # request.user = self.user
        # response = views.objects_list(request, session=0)
        # self.assertIn('Boratynka', response.content.decode())
    #
    # def test_view_objects_list_with_category(self):
    #     category = Category.objects.first()
    #     request = HttpRequest()
    #     request.user = self.client_aleo
    #     response = views.objects_list(request, category.slug, session=0)
    #     self.assertIn('Boratynka', response.content.decode())
    #
    # def test_view_objects_list_pagination(self):
    #     request = HttpRequest()
    #     request.user = self.client_aleo
    #     response = views.objects_list(request, sort='name', session=0 )
    #     self.assertIn('<strong>1</strong>', response.content.decode())

    def test_view_object_detail(self):
        request = HttpRequest()
        request.user = self.user
        first_item = Rzeczy.objects.first()
        response = views.object_detail(request, id=first_item.pk)
        self.assertIn('a frequently found coin', response.content.decode())
