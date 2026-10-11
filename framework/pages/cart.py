
from selenium.webdriver.common.by import By
import time


class cartpage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.checkout_button = (By.ID, "checkout")
        self.cart_items = (By.CLASS_NAME, "cart_item")
        self.remove_backpack = (By.ID, "remove-sauce-labs-backpack")

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def remove_backpack_item(self):
        self.driver.find_element(*self.remove_backpack).click()
        time.sleep(1)

    def continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()
        time.sleep(2)

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        time.sleep(2)