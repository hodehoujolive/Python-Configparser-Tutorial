import unittest
from selenium import webdriver
from pages.login_page import LoginPage
from utils.config_reader import read_config, read_config_section
import time , json
#from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions

class TestLogin(unittest.TestCase):
    
    def setUp(self):
        browser_os_list = read_config_section('BROWSER_OS_LIST')
        self.drivers = []
        for browser_os in browser_os_list.values():

            lt_options = {
            "user": read_config('LAMBDATEST', 'username'),
            "accessKey": read_config('LAMBDATEST', 'access_key'),
            "build": "Python Configparser Tutorial",
            "name": "Python Configparser Tutorial",
            "platformName": json.loads(browser_os)["platformName"],
            "w3c": True,
            "browserName": json.loads(browser_os)["browserName"],
            "browserVersion": json.loads(browser_os)["browser_Version"],
            "selenium_version": "4.8.0"
            }

            browser_options = EdgeOptions()
            browser_options.set_capability('LT:Options', lt_options)
            
            driver = webdriver.Remote(
                command_executor="http://hub.lambdatest.com:80/wd/hub",
                options=browser_options)

            driver.get(read_config('WEBSITE', 'url'))
            driver.maximize_window()
            self.drivers.append(driver)

    
    def tearDown(self):
        for driver in self.drivers:
            driver.quit()

    def test_login(self):
        for driver in self.drivers:
            login_page = LoginPage(driver)
            login_page.login()
            time.sleep(10)

if __name__ == '__main__':
    unittest.main()
