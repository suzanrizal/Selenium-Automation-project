from selenium import webdriver
import pytest
from pages.inventory import inventorypage
from pages.login import loginpage

def test_home(driver):
    login_obj=loginpage(driver)
    login_obj.open_url("https://www.saucedemo.com/")
    login_obj.enter_username("standard_user")
    login_obj.enter_password("secret_sauce")
    login_obj.click_login()

    obj = inventorypage(driver)

    obj.sort_products()
    obj.add_fleece_jacket()
    obj.add_backpack()
    obj.add_onesie()

    assert obj.get_cart_count() == "3"

    obj.open_cart()