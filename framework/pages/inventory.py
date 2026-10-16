
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
class inventorypage:
    def __init__(self, driver):
        self.driver = driver
        # Locators
        self.sort_dropdown = (By.XPATH, "//select[@aria-label='Sort products']")
        self.fleece_jacket = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
        self.backpack = (By.ID, "add-to-cart-sauce-labs-backpack")
        self.onesie = (By.ID, "add-to-cart-sauce-labs-onesie")
        self.cart_link = (By.CLASS_NAME, "shopping_cart_link")
        self.cart_badge = (By.CLASS_NAME, "shopping_cart_badge")

    def sort_products(self):
        dropdown = self.driver.find_element(*self.sort_dropdown)
        Select(dropdown).select_by_value("hilo")
        time.sleep(2)

    def add_fleece_jacket(self):
        self.driver.find_element(*self.fleece_jacket).click()
        time.sleep(1)

    def add_backpack(self):
        self.driver.find_element(*self.backpack).click()
        time.sleep(1)

    def add_onesie(self):
        self.driver.find_element(*self.onesie).click()
        time.sleep(1)

    def get_cart_count(self):
        return self.driver.find_element(*self.cart_badge).text

    def open_cart(self):
        self.driver.find_element(*self.cart_link).click()
        time.sleep(2)