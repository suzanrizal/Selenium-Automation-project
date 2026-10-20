import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
import time
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
from Utilities.CSVutils import CSVfiles

class Test_001_Login:

    # without config.ini file we had hardcoded info 
    # baseURL = "https://admin.demo.ecommerce.endpointdev.com/"
    # username = "admin"
    # password = "Password123!"

    # reading common information from config.ini file
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getUsername()
    password = readconfig.getpassword()

    logger = LogGen.loggen()

    def test_homePageTitle(self, driver):
        self.logger.info("************ Test_001_Login **********")
        self.logger.info("************ Verifying Homepage Title **********")
        self.driver = driver
        self.driver.get(self.baseURL)
        actual_title = self.driver.title

        if actual_title == "Login - End Point Ecommerce - Admin Portal":
            assert True
            self.logger.info("************ Homepage Title Test passed **********")
        else:
            self.driver.save_screenshot("Screenshots/test_homePageTitle.png")
            self.logger.error("************ Homepage Title Test Failed **********")
            assert False
        
            
        

        
    # def test_login(self, driver):
    #     self.logger.info("************ Verifying Login Test **********")
    #     self.driver = driver
    #     self.driver.get(self.baseURL)

    #     self.obj = Loginpage(self.driver)
    #     self.obj.setUserName(self.username)
    #     self.obj.setPassword(self.password)
    #     self.obj.clickLogin()
    #     time.sleep(2)
    #     actual_title =self.driver.title

    #     if actual_title == "Dashboard - End Point Ecommerce - Admin Portal":
    #         assert True
    #         self.logger.info("************ Login Test Passed **********")
    #     else:
    #         self.driver.save_screenshot("Screenshots/test_login.png")
    #         self.logger.error("************ Login Test Failed **********")
    #         assert False 



    
            
        






