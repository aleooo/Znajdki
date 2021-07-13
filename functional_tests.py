from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_catalog(self):
        self.browser.get('http://127.0.0.1:8000/en/')
        self.browser.implicitly_wait(3)
        assert 'Logowanie' in self.browser.title
        assert 'http://127.0.0.1:8000/en/login/' in self.browser.current_url
        self.browser.find_element_by_id('id_username').send_keys('aleo')
        self.browser.find_element_by_id('id_password').send_keys('aleoaleo')
        self.browser.find_element_by_tag_name('button').click()

        assert 'http://127.0.0.1:8000/en/' in self.browser.current_url
        self.browser.find_element_by_link_text('Add an object').click()
        assert 'http://127.0.0.1:8000/en/add/' in self.browser.current_url
        # print(Select(self.browser.find_element_by_id('id_category')).select_by_index(1))
        self.browser.find_element_by_css_selector('#id_category [value="1"]').click()
        self.browser.find_element_by_id('id_name').send_keys('FUNCTIONAL_TEST')
        self.browser.find_element_by_id('id_year').send_keys('9999')
        self.browser.find_element_by_id('id_text').send_keys('Nauka to potęgi klucz')
        self.browser.find_element_by_class_name('map').click()
        self.browser.find_element_by_id('button_create').click()


        print('test')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
