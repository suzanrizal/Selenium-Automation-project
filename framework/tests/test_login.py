from selenium import webdriver
import pytest
from pages.login import loginpage

@pytest.fixture()

def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    obj= loginpage(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username("standard_user")
    obj.enter_password("secret_sauce")
    obj.click_login()
