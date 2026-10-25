import pytest
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
import time
from Utilities.email_generator import emailgenerator


class Test_003_AddCustomer:
    baseURL = readconfig.getapplicationURL()
    username = readconfig.getUsername()
    password = readconfig.getpassword()

    logger = LogGen.loggen()

    def test_AddCustomer(self, driver):
        self.logger.info("**********Test 003 Add Customer *********")
        self.driver = driver
        self.driver.get(self.baseURL)

        self.Lobj = Loginpage(self.driver)
        self.Lobj.setUserName(self.username)
        self.Lobj.setPassword(self.password)
        self.Lobj.clickLogin()

        self.logger.info("******** Login Sucessful ********")

        self.logger.info("********* Starting Add Customer Test **********")

        self.ACobj = AddCustomer(self.driver)
        self.ACobj.clickCustomer()
        self.ACobj.clickAddCustomer()

        self.logger.info("********** Providing Customer Info ********")

        self.ACobj.setFirstName("Rahul")
        self.ACobj.setLastName("Neupane")

        self.Email = emailgenerator()   # Generating Random email and saving into Email variable

        self.ACobj.setEmail(self.Email)  #Using the Random email  

        self.ACobj.clickSave()
        time.sleep(2)

        self.logger.info("*********** Saving Customer Info **********")
        if driver.current_url == "https://admin.demo.ecommerce.endpointdev.com/Customers":
            assert True
            self.logger.info("*********** Add Customer Test Passed ***********")

        else:
            self.driver.save_screenshot("Screenshots/AddCustomer.png")
            self.logger.error("********** Add Customer Failed ***********")
            assert False






        


    