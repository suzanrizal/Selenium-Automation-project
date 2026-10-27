import pytest
from pageObjects.AddCustomerPage import AddCustomer
from pageObjects.LoginPage import Loginpage
from Utilities.readProperties import readconfig
from Utilities.customLogger import LogGen
import time
from pageObjects.add_Product import AddProduct, ScrollDown


class Test_004_AddProduct:
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

        # Add product test start
        self.logger.info("********** Add product Test Starting... ********")

        self.APobj = AddProduct(self.driver)
        self.APobj.clickProduct()
        self.APobj.clickAddToProduct()
        self.APobj.setName("Current")
        self.APobj.setSKU("Current")
        self.APobj.SelectCategoryDropdown()
        self.APobj.EnabledCheckbox()
        time.sleep(2)

        #Scroll the page
        self.Scrollobj = ScrollDown(self.driver)
        self.Scrollobj.Scroll500()
        time.sleep(2)

        self.APobj.setDescription("Current Noodles is a tasty and convenient instant noodle snack, perfect for satisfying hunger anytime with its delicious flavor and quick preparation.")
        self.APobj.DescriptionHeadingDropdown()
        self.APobj.setHeading2()
        time.sleep(2)
        self.APobj.SetShortDescription("Current noodles is very Unhealthy")
        
        self.APobj.SetWeight("75")
        self.APobj.SetBasePrice("50")
        self.Scrollobj.Scroll500()
        time.sleep(2)
        self.APobj.IsDiscountedCheckbox()
        time.sleep(2)


        self.APobj.SetDiscountedAmount("10")
        self.APobj.SetURL("www.Currentnoodles.com")
        self.APobj.SetMetaTitle("Current Noodles – Tasty and Delicious Instant Noodles")
        self.APobj.SetMetaKeywoards("Current Noodles, instant noodles, tasty noodles, quick snacks, noodle brand, instant food")
        self.APobj.SetMetaDescription("Enjoy Current Noodles, a delicious and convenient instant noodle snack perfect for quick meals and satisfying your hunger anytime.")
        self.Scrollobj.Scroll500()
        self.APobj.SetMainImage()
        self.APobj.SetThumnailImage()
        self.APobj.SetAddditionalImage()
        self.Scrollobj.ScrollToSave()
        time.sleep(2)
        self.APobj.SaveButton()
        print("Product Saved sucessfully")
        
