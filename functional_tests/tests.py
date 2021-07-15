from django.test import LiveServerTestCase
from selenium import webdriver


class NewVisitorTest(LiveServerTestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_register(self):
        self.browser.get(self.live_server_url)

        assert 'Logowanie' in self.browser.title
        assert '/en/login/' in self.browser.current_url
        self.browser.find_element_by_link_text('Sign in').click()

        self.assertURLEqual(self.browser.current_url, '/en/register/')

        self.browser.find_element_by_id('id_username').send_keys('aleo')
        self.browser.find_element_by_id('id_email').send_keys('aalala@gmail.com')
        self.browser.find_element_by_id('id_password').send_keys('aleoaleo')
        self.browser.find_element_by_id('id_confirm_password').send_keys('aleoaleo')
        self.browser.find_element_by_tag_name('button').click()



    def test_catalog(self):
        self.browser.get('poszukiwania:objects_list')
        assert 'Detectorist Catalog' in self.browser.title


        self.browser.find_element_by_id('add_object_link').click()

        assert '/en/add/' in self.browser.current_url
        # print(Select(self.browser.find_element_by_id('id_category')).select_by_index(1))
        self.browser.find_element_by_css_selector('#id_category [value="1"]').click()
        self.browser.find_element_by_id('id_name').send_keys('FUNCTIONAL_TEST')
        self.browser.find_element_by_id('id_year').send_keys('9999')
        self.browser.find_element_by_id('id_text').send_keys('Nauka to potęgi klucz')
        self.browser.find_element_by_class_name('map').click()
        self.browser.find_element_by_id('button_create').click()
        print('test')


