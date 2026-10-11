from selenium import webdriver
import pytest
from pages.home import Inventorypage
from pages.login import Loginpage

@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_home(driver):
    login_obj=Loginpage(driver)
    login_obj.open_url("https://www.saucedemo.com/")
    login_obj.enter_username("standard_user")
    login_obj.enter_password("secret_sauce")
    login_obj.click_login()
    obj=Inventorypage(driver)
    obj.click_addtocart()