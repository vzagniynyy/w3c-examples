import unittest
import os
from selenium import webdriver


class TestW3COptions(unittest.TestCase):

    def setUp(self):
        sauce_username = os.environ["SAUCE_USERNAME"]
        sauce_access_key = os.environ["SAUCE_ACCESS_KEY"]
        remote_url = "http://{}:{}@ondemand.saucelabs.com/wd/hub".format(sauce_username, sauce_access_key)

        sauceOptions = {
            "screenResolution": "1280x768",
            "platformName": "Windows 10",
            "browserVersion": "60.0",
            "seleniumVersion": "3.11.0",
            'name': 'Unittest Firefox W3C Sample'
        }

        caps =  {
            'platformName':"Windows 10",
            'browserName': "firefox",
            'browserVersion': '60.0',
            'sauce:options': sauceOptions
        }

        self.driver = webdriver.Remote(remote_url, desired_capabilities=caps)

    def tearDown(self):
        #driver.execute_script('sauce:job-result={}'.format(report.outcome))
        self.driver.quit()

    def test_should_open_safari(self):
        self.driver.get("http://www.saucedemo.com")
        actual_title = self.driver.title
        expected_title = "Swag Labs"
        assert expected_title == actual_title
