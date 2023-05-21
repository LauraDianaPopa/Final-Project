from telnetlib import EC
from time import sleep


from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.support import expected_conditions as EC

from browser import Browser
from selenium import webdriver
from selenium.webdriver.common.by import By




class SignUpPage(Browser):
    SIGN_UP = (By.LINK_TEXT, "Sign up.")
    BUSINESS_BUTTON = (By.XPATH, "//input[@value='business']")
    PERSONAL_BUTTON = (By.XPATH, "//input[@value='personal']")
    CONTINUE_BUTTON = (By.XPATH, "//span[normalize-space()='CONTINUE']")
    FIRST_NAME = (By.XPATH, "//input[@placeholder='Type your answer here...']")
    LAST_NAME = (By.XPATH, "//input[@placeholder='Type your answer here...']")
    EMAIL = (By.XPATH, "//input[@placeholder='Type your answer here...']")
    ERROR_NOTIFICATION = (By.TAG_NAME, "p")
    PASSWORD = (By.XPATH, "//input[@placeholder='Type your answer here...']")


    def navigate_to_sign_up_page(self):
        self.driver.get("https://jules.app/sign-in")

    def test_url(self):
        expected_url = "https://jules.app/sign-in"
        actual_url = self.driver.current_url
        assert actual_url == expected_url, f'URL incorect :{actual_url}'

    def test_page_title(self):
        actual_title = self.driver.title
        expected_title = "Jules"
        assert actual_title == expected_title, "Titlul paginii nu este corect"

    def sign_up(self):
        self.driver.find_element(*self.SIGN_UP).click()
        sleep(1)

    def click_Bussines_button(self):
        self.driver.find_element(*self.BUSINESS_BUTTON).click()
        sleep(1)

    def click_Personal_button(self):
        self.driver.find_element(*self.PERSONAL_BUTTON).click()
        sleep(1)


    def continue_button(self):
        self.driver.find_element(*self.CONTINUE_BUTTON).click()
        sleep(1)
    def test_first_name(self, first_name):
        self.driver.find_element(*self.FIRST_NAME).send_keys("Laura")
        expected = "Laura"
        actual = first_name
        assert actual == expected, f"Textul introdus nu este cel asteptat actual={actual}"


    def enter_after_first_name(self):
        self.driver.find_element(*self.FIRST_NAME).send_keys(Keys.ENTER)
        sleep(1)

    def test_last_name(self, last_name):
        self.driver.find_element(*self.LAST_NAME).send_keys("Popa")
        expected = "Popa"
        actual = last_name
        assert actual == expected, f"Textul introdus nu este cel asteptat actual={actual}"

    def enter_after_last_name(self):
        self.driver.find_element(*self.LAST_NAME).send_keys(Keys.ENTER)
        sleep(1)

    def enter_wrong_email(self, wrong_email):
        self.driver.find_element(*self.EMAIL).send_keys(wrong_email)
        sleep(1)

    def test_error(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.ERROR_NOTIFICATION).text
        except NoSuchElementException:
            actual_message = "None"
        EC.text_to_be_present_in_element((By.TAG_NAME, "p"),expected_message)
        assert actual_message == expected_message, f'Please enter a valid email address. actual={actual_message}, expected={expected_message}'

    def clear_email_input(self):
        self.driver.find_element(*self.EMAIL).send_keys(Keys.CLEAR)

    def email_field(self, email):
        self.driver.find_element(*self.EMAIL).send_keys(email)
        sleep(1)

    def test_error_is_not_displayed_anymore(self):
        try:
            self.driver.find_element(By.TAG_NAME, "p")
        except NoSuchElementException:
            pass

    def enter_after_email_field(self):
        self.driver.find_element(*self.EMAIL).send_keys(Keys.ENTER)
        sleep(1)

    def password_field(self, password):
        self.driver.find_element(*self.PASSWORD).send_keys(password)
        sleep(1)

    def enter_after_password_field(self):
        self.driver.find_element(*self.PASSWORD).send_keys(Keys.ENTER)
        sleep(1)







