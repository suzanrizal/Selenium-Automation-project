from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
import time
from Utilities.email_generator import emailgenerator
from pageObjects.searchCustomerPage import SearchCustomer


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

        # Customer 1
        self.ACobj.setFirstName("Rahul")
        self.ACobj.setLastName("Neupane")
        self.Email = emailgenerator()
        self.ACobj.setEmail(self.Email)
        self.ACobj.clickSave()
        time.sleep(2)
        self.ACobj.clickAddCustomer()

        # Customer 2
        self.ACobj.setFirstName("Sujan")
        self.ACobj.setLastName("Rijal")
        self.Email = emailgenerator()
        self.ACobj.setEmail(self.Email)
        self.ACobj.clickSave()
        time.sleep(2)
        self.ACobj.clickAddCustomer()

        # Customer 3
        self.ACobj.setFirstName("Rahul")
        self.ACobj.setLastName("magar")
        self.Email = emailgenerator()
        self.ACobj.setEmail(self.Email)
        time.sleep(2)
        self.ACobj.clickSave()

        time.sleep(2)

        # Searching Customer and Validating
        self.logger.info("*********** Search customer started ***********")

        self.Scobj = SearchCustomer(self.driver)
        self.Scobj.SearchFirstNameField("Rahul")

        time.sleep(2)
        rows = self.Scobj.getNoOfRows()

        assert len(rows) > 0, "No customers found"

        for row in rows:
            assert "Rahul" in row.text, f"Search Failed: {row.text}"
            
         