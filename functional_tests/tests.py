import sys

from django.contrib.auth.models import User
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.support.select import Select

from poszukiwania.models import Category, Rzeczy, Map


class NewVisitorTest(StaticLiveServerTestCase):

    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.user = User.objects.create_user('aleo', 'medda@test.com', 'aletojuzbylo')
        category = Category.objects.create(title='Coins', slug='coins')
        map1 = Map.objects.create(point='{"lat": 52.01546930699952, "lng": 21.915056009813515}', description='point')
        Rzeczy.objects.create(user=self.user,
                              location=map1,
                              category=category,
                              name='Boratynka',
                              slug='boratynka',
                              year=1666,
                              text='a frequently found coin', )

    def tearDown(self):
        self.browser.quit()

    def test_1_register(self):
        self.browser.get(self.server_url)
        self.assertEqual('Log in', self.browser.title)
        self.browser.find_element_by_link_text('Sign in').click()

        self.assertEqual('Register', self.browser.title)

        self.browser.find_element_by_id('id_username').send_keys('heniek')
        self.browser.find_element_by_id('id_email').send_keys('aalala@gmail.com')
        self.browser.find_element_by_id('id_password1').send_keys('aleoaleo')
        self.browser.find_element_by_id('id_password2').send_keys('aleoaleo')
        self.browser.find_element_by_tag_name('button').click()

        self.assertEqual('Log in', self.browser.title)

        self.browser.find_element_by_id('id_username').send_keys('heniek')
        self.browser.find_element_by_id('id_password').send_keys('aleoaleo')
        self.browser.find_element_by_tag_name('button').click()

        self.assertEqual('Detectorist Catalog', self.browser.title)

    def test_create_object(self):
        self.browser.get(self.server_url)
        self.assertEqual('Log in', self.browser.title)
        self.browser.find_element_by_id('id_username').send_keys('aleo')
        self.browser.find_element_by_id('id_password').send_keys('aletojuzbylo')
        self.browser.find_element_by_tag_name('button').click()

        self.assertEqual('Detectorist Catalog', self.browser.title)

        self.browser.find_element_by_id('add_object_link').click()

        self.assertEqual('Add objects', self.browser.title)

        sel = Select(self.browser.find_element_by_id('id_category'))
        sel.select_by_visible_text('Coins')
        self.browser.find_element_by_id('id_name').send_keys('FUNCTIONAL_TEST')
        self.browser.find_element_by_id('id_year').send_keys('9999')
        self.browser.find_element_by_id('id_text').send_keys('Nauka to potęgi klucz')
        self.browser.find_element_by_class_name('map').click()
        self.browser.find_element_by_id('button_create').click()

        self.browser.find_element_by_link_text('back').click()

        self.assertEqual('Detectorist Catalog', self.browser.title)

        self.assertIn('FUNCTIONAL_TEST', self.browser.find_element_by_class_name('objects').text)

    def test_detail(self):
        self.browser.get(self.server_url)
        self.assertEqual('Log in', self.browser.title)
        self.browser.find_element_by_id('id_username').send_keys('aleo')
        self.browser.find_element_by_id('id_password').send_keys('aletojuzbylo')
        self.browser.find_element_by_tag_name('button').click()

        self.assertIn('Boratynka', self.browser.find_element_by_class_name('jasny').text)
        self.browser.find_element_by_class_name('jasny').click()

        self.assertEqual(self.browser.title, 'Detail')
        self.assertIn('Boratynka', self.browser.find_element_by_id('table_detail').text)

    # Not work
    # def test_search(self):
    #     self.browser.get(self.server_url)
    #     self.assertEqual('Log in', self.browser.title)
    #     self.browser.find_element_by_id('id_username').send_keys('aleo')
    #     self.browser.find_element_by_id('id_password').send_keys('aletojuzbylo')
    #     self.browser.find_element_by_tag_name('button').click()
    #
    #     self.browser.find_element_by_id('input_search').send_keys('B')
    #     self.browser.implicitly_wait(3)
    #     self.assertIn('Obverse', self.browser.find_element_by_class_name('light').get_attribute('outerHTML'))












