import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from Utilities.readProperties import readconfig

class Test_001_Login:

    # without config.ini file we had hardcoded info 
    # baseURL = "https://admin.demo.ecommerce.endpointdev.com/"
    # username = "admin"
    # password = "Password123!"

    # reading common information from config.ini file
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getUsername()
    password = readconfig.getpassword()

    def test_homePageTitle(Self, driver):
        Self.driver = driver
        Self.driver.get(Self.baseURL)
        actual_title = Self.driver.title

        assert actual_title == "Login - End Point Ecommerce - Admin Portal"
        

    def test_login(Self, driver):
        Self.driver = driver
        Self.driver.get(Self.baseURL)

        Self.obj = Loginpage(Self.driver)
        Self.obj.setUserName(Self.username)
        Self.obj.setPassword(Self.password)
        Self.obj.clickLogin()
        time.sleep(2)
        actual_title =Self.driver.title

        if actual_title == "Dashboard - End Point Ecommerce - Admin Porta":
            assert True
        else:
            Self.driver.save_screenshot("Screenshots/test_login.png")
            assert False , "Login failed: Dashboard title not found"
        
            
        






