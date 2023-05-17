from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.config_reader import read_config

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    @property
    def email(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'input-email')))

    @property
    def password(self):
        return self.wait.until(EC.presence_of_element_located((By.ID, 'input-password')))

    @property
    def submit_button(self):
        return self.wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@value='Login']")))

    def login(self):
        self.email.send_keys(read_config('LOGIN', 'email'))
        self.password.send_keys(read_config('LOGIN', 'password'))
        self.submit_button.click()
