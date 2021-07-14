from django.test import TestCase
from django.contrib.auth.models import User

from poszukiwania.models import Map, Category, Rzeczy


class ModelsTestCase(TestCase):

    def setUp(self):
        category = Category.objects.create(title='coins', slug='coins')
        category1 = Category.objects.create(title='buttons', slug='buttons')
        map1 = Map.objects.create(point='{"lat": 52.01546930699952, "lng": 21.915056009813515}', description='point')
        map2 = Map.objects.create(point='{"lat": 52.01546930199952, "lng": 21.915056009813516}', description='point1')
        self.user = User.objects.create_user('aleo', 'medda@test.com', 'aletojuzbylo')
        self.client.login(username='aleo', password='aletojuzbylo')
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
        category = Category.objects.first()
        first_find = Rzeczy.objects.first()
        count_map = Map.objects.count()

        self.assertEqual(count_map, 2)
        self.assertEqual(category.title, 'coins')
        self.assertEqual(first_find.name, 'Boratynka')

    def test_Rzeczy_get_absolute_url(self):
        first_find = Rzeczy.objects.first()

        response = self.client.get(first_find.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_Category_get_absolute_url(self):
        first_category = Category.objects.first()
        response = self.client.get(first_category.get_absolute_url())
        self.assertEqual(response.status_code, 200)

    def test_Map_description_f(self):
        first_map = Map.objects.get(description='point')
        self.assertIn(first_map.description_f(), 'point')

