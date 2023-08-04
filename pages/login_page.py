from telnetlib import EC

from selenium.common.exceptions import NoSuchElementException

from browser import Browser
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class LoginPage(Browser):
    EMAIL= (By.CSS_SELECTOR, 'input[placeholder="Enter your email"]')
    PASS = (By.CSS_SELECTOR, 'input[placeholder="Enter your password"]')
    LOGIN = (By.XPATH, "//button")
    FORGOT_PASS = (By.ID, 'forgot-password-link')
    PASS_1 = (By.CSS_SELECTOR, 'input[placeholder="Enter your email"]')
    SEND = (By.ID, 'login-button')

    def navigate_to_login_page(self):
        self.driver.get("https://jules.app/sign-in")

    def email_field(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def rong_password(self, rong_pass):
        self.driver.find_element(*self.PASS).send_keys(rong_pass)

    def login_button1(self):
        self.driver.find_element(*self.LOGIN).click()

    def forgot_link(self):
        self.driver.find_element(*self.FORGOT_PASS).click()

    def email_field_1(self, email):
        self.driver.find_element(*self.PASS_1).send_keys(email)

    def send_email(self):
        self.driver.find_element(*self.SEND).click()


    def email_field_2(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)


    def password_field(self, password):
        self.driver.find_element(*self.PASS).send_keys(password)

    def login_button(self):
        self.driver.find_element(*self.LOGIN).click()

