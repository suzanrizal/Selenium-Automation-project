from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select

class AddProduct:

    Product_Menu_XPATH = "//a[normalize-space()='Products']"
    Add_New_Product_Menu_XPATH = "//a[normalize-space()='Add a new product']"
    Textbox_Name_ID = "Product_Name"
    Textbox_SKU_ID = "Product_Sku"


    def __init__(self, driver = webdriver.Chrome):
        self.driver = driver

    def P