from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Chrome()
driver.maximize_window()

url = "https://formy-project.herokuapp.com/fileupload"
driver.get(url)

file_upload = driver.find_element(By.ID, "file-upload-field")
file_upload.send_keys(r"C:\Users\rizal\Downloads\452397624_521027916990532_4345181435269335923_n.jpg")
time.sleep(3)
assert file_upload.get_attribute("value"), "File was not uploaded"
print("File uploaded successfully")

driver.close()
driver.quit()



