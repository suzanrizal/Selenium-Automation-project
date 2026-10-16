from selenium.webdriver.common.by import By
from selenium import webdriver

class Loginpage:
    textbox_username_id = "Login_Username"
    textbox_password_id = "Login_Password"
    button_login_XPATH = "//button[@type='submit']"
    button_logout_XPATH = "//a[normalize-space()='Logout']"

    def __init__(self, driver: webdriver.Chrome):
        self.driver=driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID, self.textbox_username_id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID, self.textbox_password_id).send_keys(password)
        
    def clickLogin(self):
        self.driver.find_element(By.XPATH, self.button_login_XPATH).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.button_logout_XPATH).click()



    
    


        