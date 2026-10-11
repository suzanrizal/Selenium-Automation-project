
from selenium.webdriver.common.by import By
import time


class checkoutpage:
    def __init__(self, driver):
        self.driver = driver

        # Checkout information locators
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.postal_code = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")

        # Order overview locators
        self.finish_button = (By.ID, "finish")
        self.cancel_button = (By.ID, "cancel")

        # Confirmation locator
        self.success_message = (By.CLASS_NAME, "complete-header")
        self.back_home_button = (By.ID, "back-to-products")

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        time.sleep(1)

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name).send_keys(last_name)
        time.sleep(1)

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code).send_keys(postal_code)
        time.sleep(1)

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        time.sleep(2)

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
        time.sleep(2)

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text

    def click_back_home(self):
        self.driver.find_element(*self.back_home_button).click()
        time.sleep(2)

    def cancel_checkout(self):
        self.driver.find_element(*self.cancel_button).click()
        time.sleep(2)