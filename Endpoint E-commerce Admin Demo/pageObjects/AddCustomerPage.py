from selenium.webdriver.common.by import By
from selenium import webdriver

class AddCustomer:
    customer_menu_XPATH = "//a[normalize-space()='Customers']"
    Add_new_customer_button_XPATH = "//a[normalize-space()='Add a new customer']"
    textbox_first_name_ID = "Customer_Name"
    textbox_last_name_ID = "Customer_LastName"
    textbox_email_Id = "Customer_Email"
    save_button_XPATH = "//button[@formaction='/Customers/Create?handler=Save']"

    def __init__(self,driver :webdriver.Chrome):
        self.driver = driver

    def clickCustomer(self):
        self.driver.find_element(By.XPATH, self.customer_menu_XPATH).click()

    def clickAddCustomer(self):
        self.driver.find_element(By.XPATH, self.Add_new_customer_button_XPATH).click()

    def setFirstName(self, FirstName ):
        self.driver.find_element(By.ID, self.textbox_first_name_ID).send_keys(FirstName)

    def setLastName(self, LastName):
        self.driver.find_element(By.ID, self.textbox_last_name_ID).send_keys(LastName)

    def setEmail(self, Email):
        self.driver.find_element(By.ID, self.textbox_email_Id).send_keys(Email)

    def clickSave(self):
        self.driver.find_element(By.XPATH, self.save_button_XPATH).click()
        


        
