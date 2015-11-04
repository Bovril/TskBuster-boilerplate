# -*- coding: utf-8 -*-
# The first line indicates the coding of the file
from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        """ a setUp method that initializes the test. 
        It opens the browser and it waits for
        3 seconds if needs to (if the page is not loaded)
        """
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(6)

    def tearDown(self):
        self.browser.quit()

    def test_it_worked(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Welcome to Django', self.browser.title)

if __name__ == '__main__':
    unittest.main()#warnings='ignore')
