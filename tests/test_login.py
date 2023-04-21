import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config_reader import read_config
import time


class TestLogin(unittest.TestCase):
    
    def setUp(self):
    
        lambdatest_username = read_config('LAMBDATEST', 'username')
        lambdatest_access_key = read_config('LAMBDATEST', 'access_key')

        if lambdatest_username and lambdatest_access_key:
            desired_caps = {
                'LT:Options': {
                    "build": "Python ConfigParser Tutorial",
                    "name": "Python ConfigParser Tutorial",
                    "platformName": "Windows 11",
                    "selenium_version": "4.0.0",
                    "console": 'true', 
                    "network": 'true',
                },
                "browserName": "firefox",
                "browserVersion": "latest",
            }

            self.driver = webdriver.Remote(
                command_executor="http://{}:{}@hub.lambdatest.com/wd/hub".format(
                    lambdatest_username, lambdatest_access_key),
                desired_capabilities=desired_caps)
        else:
            browser_name = read_config('BROWSER', 'name')
            if browser_name.lower() == 'chrome':
                self.driver = webdriver.Chrome()
            elif browser_name.lower() == 'firefox':
                self.driver = webdriver.Firefox()
            elif browser_name.lower() == 'edge':
                self.driver = webdriver.Edge()
            else:
                raise ValueError('Invalid browser name')

        self.driver.get(read_config('WEBSITE', 'url'))
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()

    def test_login(self):
        login_page = LoginPage(self.driver)
        login_page.login()
        time.sleep(10)

if __name__ == '__main__':
       unittest.main()
