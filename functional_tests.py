from selenium import webdriver
from selenium.webdriver.support.select import Select
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_catalog(self):
        self.browser.get('http://127.0.0.1:8000/')
        self.browser.implicitly_wait(3)
        assert 'Detectorist Catalog' in self.browser.title
        hyperlink_login = self.browser.find_element_by_tag_name('a')
        assert 'Login' in hyperlink_login.text
        hyperlink_login.click()
        assert 'http://127.0.0.1:8000/login/' in self.browser.current_url
        self.browser.find_element_by_id('id_username').send_keys('aleo')
        self.browser.find_element_by_id('id_password').send_keys('aleoaleo')
        self.browser.find_element_by_tag_name('button').click()

        assert 'http://127.0.0.1:8000/catalog/' in self.browser.current_url
        self.browser.find_element_by_link_text('Add an object').click()
        assert 'http://127.0.0.1:8000/add/' in self.browser.current_url
        # print(Select(self.browser.find_element_by_id('id_category')).select_by_index(1))
        self.browser.find_element_by_css_selector('#id_category [value="1"]').click()
        self.browser.find_element_by_id('id_name').send_keys('FUNCTIONAL_TEST')
        self.browser.find_element_by_id('id_year').send_keys('9999')
        self.browser.find_element_by_id('id_text').send_keys('Nauka to potęgi klucz')
        self.browser.find_element_by_class_name('ol-unselectable').click()
        self.browser.find_element_by_tag_name('button').click()
        print(self.browser.find_element_by_class_name('errorlist').text)

        print('test')



if __name__ == '__main__':
    unittest.main(warnings='ignore')
