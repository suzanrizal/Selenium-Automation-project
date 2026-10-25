from selenium.webdriver.common.by import By
from selenium import webdriver

class SearchCustomer:

    search_customer_field_ID = "dt-search-0"
    Table_XPATH = "//*[@id='table-customers_wrapper']/div[2]/div"
    Table_Rows_XPATH = "//*[@id='table-customers']/tbody/tr"
    # Table_Column_XPATH = "//*[@id='table-customers']/tbody/tr/td"

    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver

    def SearchFirstNameField(self, FirstName):
        self.driver.find_element(By.ID, self.search_customer_field_ID).clear()
        self.driver.find_element(By.ID, self.search_customer_field_ID).send_keys(FirstName)

    def searchLastNameField(self, LastName):
        self.driver.find_element(By.ID, self.search_customer_field_ID).clear()
        self.driver.find_element(By.ID, self.search_customer_field_ID).send_keys(LastName)

    def searchEmailField(self, Email):
        self.driver.find_element(By.ID, self.search_customer_field_ID).clear()
        self.driver.find_element(By.ID, self.search_customer_field_ID).send_keys(Email)

    def getNoOfRows(self):
        return self.driver.find_elements(By.XPATH, self.Table_Rows_XPATH)




    