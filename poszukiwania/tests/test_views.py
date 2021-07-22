from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User

from poszukiwania.models import Map, Category, Rzeczy


class ViewsTestCase(TestCase):
    def setUp(self):
        category_coins = Category.objects.create(title='coins', slug='coins')
        category_buttons = Category.objects.create(title='buttons', slug='buttons')
        map1 = Map.objects.create(point='{"lat": 52.01546930699952, "lng": 21.915056009813515}', description='point')
        map2 = Map.objects.create(point='{"lat": 52.01546930199952, "lng": 21.915056009813516}', description='point1')
        self.user = User.objects.create_user('aleo', 'medda@test.com', 'aletojuzbylo')
        self.client.login(username='aleo', password='aletojuzbylo')
        Rzeczy.objects.create(user=self.user,
                              location=map1,
                              category=category_coins,
                              name='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='a frequently found coin', )

        Rzeczy.objects.create(user=self.user,
                              location=map2,
                              category=category_buttons,
                              name='wz19',
                              slug='wz19',
                              year=1919,
                              text='a rarely found button', )

    def test_objects_list_(self):
        response = self.client.get(reverse('poszukiwania:objects_list'))
        self.assertContains(response, '<div class="float_left text-justify"><h4>')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Boratynka')

    def test_objects_list_pagination(self):
        response = self.client.get(reverse('poszukiwania:objects_list'))
        self.assertContains(response, '<a class="page-link" href="#">1</a>')

    def test_objects_list_with_category(self):
        category = Category.objects.get(title='buttons')
        response = self.client.get(reverse('poszukiwania:objects_list_by_category', args=[category.slug]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'wz19')

    def test_objects_list_style_table(self):
        response = self.client.post(reverse('poszukiwania:style', args=['table']))
        self.assertRedirects(response, '/en/')
        response = self.client.get(reverse('poszukiwania:objects_list'))
        self.assertContains(response, '<th class="tdth">Name</th>')

    def test_object_detail(self):
        first_item = Rzeczy.objects.first()
        response = self.client.get(first_item.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'a frequently found coin')
