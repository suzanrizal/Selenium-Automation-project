import pytest
from selenium import webdriver
from pageObjects.LoginPage import Loginpage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
from Utilities.CSVutils import CSVfiles

class Test_002_DDT_Login:
        baseURL = readconfig.getapplicationURL()
        logger = LogGen.loggen()
     # Data Driven testing 
        @pytest.mark.parametrize(
        "username,password,exp",
                CSVfiles.get_login_data()
        )
        def test_login(self,driver,username,password,exp):
            self.logger.info("********** Verifying Login Test*******")
    
            self.driver = driver
            self.driver.get(self.baseURL)
            
            self.obj = Loginpage(self.driver)
            self.obj.setUserName(username)
            self.obj.setPassword(password)
            self.obj.clickLogin()
    
            actual_title = self.driver.title
            expected_title = "Dashboard - End Point Ecommerce - Admin Portal"
    
            if exp.lower() == "pass":
                assert actual_title == expected_title, \
                f"Login succeed for username: {username}"
                self.logger.info("********* Login Test Passed ********")
    
            elif exp.lower() == "fail":
                assert actual_title != expected_title, \
                f"Login Failed For Username: {username}"
                self.logger.info("******** Login Test Passed: Invalid Login Rejected *******")
    
            else:
                pytest.fail(f"Invalid Expected result in CSV: {exp}")

