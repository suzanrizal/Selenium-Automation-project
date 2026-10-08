from selenium import webdriver
import pytest
from pages.login import loginpage

@pytest.mark.parametrize("username, password", [
    ("standard_user","secret_sauce"),
    ("Fakeuser","fakepass"),
    ("invalid_user","invalid_password")
    ])

def test_login(driver, username, password):
    obj= loginpage(driver)
    obj.open_url("https://www.saucedemo.com/")
    obj.enter_username(username)
    obj.enter_password(password)
    obj.click_login()
    assert "inventory" in driver.current_url, "Login failed: User is not redirected to inventory page"

# def test_invalid_login(driver):
#     obj= loginpage(driver)
#     obj.open_url("https://www.saucedemo.com/")
#     obj.enter_username("Sujan_rijal")
#     obj.enter_password("_Fake")
#     obj.click_login()
#     assert "inventory" not in driver.current_url, "Login should have failed but it succeeded"
