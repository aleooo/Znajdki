from django.test import TestCase, Client
from django.urls import reverse, resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.contrib.auth.models import User


from poszukiwania import views
from poszukiwania.models import Map, Category, Rzeczy


class ViewsTestCase(TestCase):
#     def setUp(self):
#         self.user = self.client.login(username='aleo', password='aletojuzbylo')

    def test_view_rzeczy_list(self):
        request = HttpRequest()
        self.client.login(username='aleo', password='aletojuzbylo')
        response = self.client.get(reverse('poszukiwania:objects_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Boratynka')

#     def test_view_objects_list_with_category(self):
#         category = Category.objects.first()
#         request = HttpRequest()
#         request.user = self.user
#         response = views.objects_list(request, category.slug, session=0)
#         self.assertIn('Boratynka', response.content.decode())
#
#     def test_view_objects_list_pagination(self):
#         request = HttpRequest()
#         request.user = self.user
#         response = views.objects_list(request, sort='name', session=0 )
#         self.assertIn('<strong>1</strong>', response.content.decode())
#
#     def test_view_object_detail(self):
#         request = HttpRequest()
#         request.user = self.user
#
#         response = views.object_detail(request, id=5)
#         self.assertIn('a frequently found coin', response.content.decode())
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
