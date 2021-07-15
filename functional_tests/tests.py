from django.contrib.auth.models import User
from django.test import LiveServerTestCase
from selenium import webdriver

class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        User.objects.create_user('aleo', 'medda@test.com', 'aletojuzbylo')

    def tearDown(self):
        self.browser.quit()

    def test_1_register(self):


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

        self.assertEqual('Log in', self.browser.title)
        self.browser.find_element_by_id('id_username').send_keys('aleo')
        self.browser.find_element_by_id('id_password').send_keys('aletojuzbylo')
        self.browser.find_element_by_tag_name('button').click()

        self.assertEqual('Detectorist Catalog', self.browser.title)

        self.browser.find_element_by_id('add_object_link').click()

        self.assertEqual('Add objects', self.browser.title)

        self.browser.find_element_by_css_selector('#id_category').click()
        self.browser.find_element_by_id('id_name').send_keys('FUNCTIONAL_TEST')
        self.browser.find_element_by_id('id_year').send_keys('9999')
        self.browser.find_element_by_id('id_text').send_keys('Nauka to potęgi klucz')
        self.browser.find_element_by_class_name('map').click()
        self.browser.find_element_by_id('button_create').click()

        self.browser.find_element_by_link_text('back').click()

        self.assertEqual('Detectorist Catalog', self.browser.title)









