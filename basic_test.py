# -*- coding: utf-8 -*-
import os
from time import sleep
# from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest
from pyvirtualdisplay import Display

def get_base_url():
    branch_name = os.getenv('BRANCH_NAME', '')
    if branch_name != 'saas-stage':
        return 'https://%s.preply.com' % os.getenv('BRANCH_NAME', '')
    return 'https://saas.preply.com'

class TestExample(unittest.TestCase):

    def setUp(self):
        self.display = Display(visible=0, size=(800, 600))
        self.display.start() # for server should be uncomented
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = get_base_url()
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_example(self):
        driver = self.driver
        driver.get(self.base_url)
        driver.get(self.base_url)
        driver.get(self.base_url + "/ua/New-York-City-NY/repetitory--angliyskogo")
        driver.get(self.base_url + "/ua/repetytor/1/")
        print self.base_url
        assert self.base_url == 'https://stage2.preply.com'
        driver.quit()
        self.display.stop()

    def test_example2(self):
        driver = self.driver
        driver.get(self.base_url + "/ua/repetytor/1/")

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
