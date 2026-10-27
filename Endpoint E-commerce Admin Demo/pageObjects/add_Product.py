from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

class AddProduct:

    Product_Menu_XPATH = "//a[normalize-space()='Products']"
    Add_New_Product_Menu_XPATH = "//a[normalize-space()='Add a new product']"
    Textbox_Name_ID = "Product_Name"
    Textbox_SKU_ID = "Product_Sku"
    category_dropdown_ID = "Product_CategoryId"
    enabled_checkbox_ID = "Product_IsEnabled"
    is_in_stock_checkbox = "Product_IsInStock"

    DescriptionEditor_CSS = "#product-description-editor .ql-editor"
    DescriptionToolbar_CSS = "div.ql-toolbar"
    HeadingDropdown_CSS = ".ql-header .ql-picker-label"
    Heading2_CSS = ".ql-header .ql-picker-item[data-value='2']"

    Description_textbox_CLASS = "ql-editor"

    short_description_ID = "Product_ShortDescription"
    textbox_weight_ID = "Product_Weight"
    Base_price_ID = "Product_BasePrice"
    checkbox_is_discounted = "Product_IsDiscounted"
    textbox_discounted_amount_id = "Product_DiscountAmount"
    textbox_URL_ID = "Product_UrlKey"
    textbox_meta_title_ID = "Product_MetaTitle"
    textbox_meta_keywoard_ID = "Product_MetaKeywords"
    textbox_meta_Description_ID = "Product_MetaDescription"
    upload_image_main_ID = "Product_MainImageFile"
    upload__image_thumnail_ID = "Product_ThumbnailImageFile"
    upload_image_additionals = "new-product-additional-image-file"
    save_button_XPATH = "//button[@formaction='/Products/Create?handler=Save']"

    def __init__(self,driver = webdriver.Chrome):
        self.driver = driver

    def clickProduct(self):
        self.driver.find_element(By.XPATH, self.Product_Menu_XPATH).click()
        
    def clickAddToProduct(self):
        self.driver.find_element(By.XPATH, self.Add_New_Product_Menu_XPATH).click()

    def setName(self, Name):
        self.driver.find_element(By.ID, self.Textbox_Name_ID).clear()        
        self.driver.find_element(By.ID, self.Textbox_Name_ID).send_keys(Name)

    def setSKU(self, SKU):
        self.driver.find_element(By.ID, self.Textbox_SKU_ID).clear()       
        self.driver.find_element(By.ID, self.Textbox_SKU_ID).send_keys(SKU)

    def SelectCategoryDropdown(self):
        dropdown = self.driver.find_element(By.ID, self.category_dropdown_ID)
        select = Select(dropdown)
        select.select_by_value("4")

    def EnabledCheckbox(self):
        self.driver.find_element(By.ID, self.enabled_checkbox_ID).click()

    def IsInStockCheckbox(self):
        self.driver.find_element(By.ID, self.is_in_stock_checkbox).click()

    def DescriptionHeadingDropdown(self):
        self.driver.find_element(By.CSS_SELECTOR, self.description_heading_dropdown_CSS).click()

    def setHeading2(self):
        self.driver.find_element(By.CSS_SELECTOR , self.Heading2_CSS).click()

    def setDescription(self, text):
        wait = WebDriverWait(self.driver, 10)

        editor = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, self.DescriptionEditor_CSS)))
        editor.click()
        editor.send_keys(text)

    def DescriptionHeadingDropdown(self):
        self.driver.find_element(
        By.CSS_SELECTOR, self.HeadingDropdown_CSS).click()


    def setHeading2(self):
        wait = WebDriverWait(self.driver, 10)

        heading2 = wait.until(
        EC.element_to_be_clickable(
            (By.CSS_SELECTOR, self.Heading2_CSS)
        )
        )
        heading2.click()

#     def DescriptionHeadingDropdown(self):
#         wait = WebDriverWait(self.driver, 10)

#         dropdown = wait.until(
#         EC.element_to_be_clickable(
#             (By.CSS_SELECTOR, self.DescriptionHeadingDropdown_CSS)
#         )
#     )
#         dropdown.click()


# def setHeading2(self):
#     wait = WebDriverWait(self.driver, 10)

#     heading2 = wait.until(
#         EC.element_to_be_clickable(
#             (By.CSS_SELECTOR, self.Heading2_CSS)
#         )
#     )
#     heading2.click()

    def SetDescription(self, Description):
        self.driver.find_element(By.CLASS_NAME, self.Description_textbox_CLASS).send_keys(Description)

    def SetShortDescription(self, ShortDescription):
        self.driver.find_element(By.ID, self.short_description_ID).send_keys(ShortDescription)

    def SetWeight(self, Weight):
        self.driver.find_element(By.ID, self.textbox_weight_ID).send_keys(Weight)

    def SetBasePrice(self, BasePrice):
        self.driver.find_element(By.ID, self.Base_price_ID).send_keys(BasePrice)

    def IsDiscountedCheckbox(self):
        self.driver.find_element(By.ID, self.checkbox_is_discounted).click()

    def SetDiscountedAmount(self, DiscountAmount):
        self.driver.find_element(By.ID , self.textbox_discounted_amount_id).send_keys(DiscountAmount)

    def SetURL(self, URL):
        self.driver.find_element(By.ID, self.textbox_URL_ID).send_keys(URL)

    def SetMetaTitle(self, MetaTitle):
        self.driver.find_element(By.ID, self.textbox_meta_title_ID).send_keys(MetaTitle)

    def SetMetaKeywoards(self, MetaKeywoards):
        self.driver.find_element(By.ID, self.textbox_meta_keywoard_ID).send_keys(MetaKeywoards)

    def SetMetaDescription(self, MetaDescription):
        self.driver.find_element(By.ID, self.textbox_meta_Description_ID).send_keys(MetaDescription)

    def SetMainImage(self):
        self.driver.find_element(By.ID, self.upload_image_main_ID).send_keys(r"C:\Users\rizal\Downloads\current-hot-n-spicy.png")

    def SetThumnailImage(self):
        self.driver.find_element(By.ID, self.upload__image_thumnail_ID).send_keys(r"C:\Users\rizal\Downloads\current-hot-n-spicy.png")

    def SetAddditionalImage(self):
        self.driver.find_element(By.ID, self.upload_image_additionals).send_keys(r"C:\Users\rizal\Downloads\current-hot-n-spicy.png")

    
    def SaveButton(self):
        self.driver.find_element(By.XPATH, self.save_button_XPATH).click()

class ScrollDown:

    save_button_XPATH = "//button[@formaction='/Products/Create?handler=Save']"

    def __init__(self,driver = webdriver.Chrome):
        self.driver = driver

    def Scroll500(self):
        self.driver.execute_script("window.scrollBy(0, 500);")

    # Scrolling to element
    def ScrollToSave(self):
        element = self.driver.find_element(By.XPATH, self.save_button_XPATH)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

        

    