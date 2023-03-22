from telnetlib import EC

from selenium.common.exceptions import NoSuchElementException

from browser import Browser
from selenium.webdriver.common.by import By


class LoginPage(Browser):
    EMAIL= (By.CSS_SELECTOR, 'input[placeholder="Enter your email"]')
    PASS = (By.CSS_SELECTOR, 'input[placeholder="Enter your password"]')
    LOGIN = (By.XPATH, "//button")




    def navigate_to_login_page(self):
        self.driver.get("https://jules.app/sign-in")


    def email_field(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)

    def password_field(self, password):
        self.driver.find_element(*self.PASS).send_keys(password)

    def login_button(self):
        self.driver.find_element(*self.LOGIN).click()


