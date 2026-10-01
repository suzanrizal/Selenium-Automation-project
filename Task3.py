from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
time.sleep(2)
wait = WebDriverWait(driver, 10)

url = "https://sagar-test-qa.vercel.app/contact.html"
driver.get(url)
time.sleep(2)

# test = wait.until(
#     EC.element_to_be_clickable((By.XPATH, "/html/body/div/article/ul/li[3]/a"))
# )
# assert test.is_displayed(), "Test link is not displayed"
# test.click()
try:
    your_name = wait.until(
        EC.element_to_be_clickable((By.ID, "name"))
        )
    your_name.send_keys("Sujan rijal")
except Exception as e:
    print("Name field is not displayed", e)

try:
    email = wait.until(
        EC.element_to_be_clickable((By.ID, "email"))
    )
    email.send_keys("rizaluszan3@gmail.com")

except Exception as e:
    print("Email field is not displayed", e)

try:
    message = wait.until(
    EC.element_to_be_clickable((By.ID, "message"))
    )
    message.send_keys("I am sujan rijal, a passionate software tester with a strong background in quality assurance and automation testing. I have experience in various testing methodologies, including functional, regression, and performance testing. I am skilled in using tools like Selenium, JIRA, and TestRail to ensure the delivery of high-quality software products. I am always eager to learn new technologies and improve my skills to contribute effectively to the success of the team and organization.")
    
except Exception as e:
    print("Message field is not displayed", e)

try:
    send_message = wait.until(
    EC.element_to_be_clickable((By.XPATH, "//*[@id='contactForm']/button"))
)
    send_message.click()

except Exception as e:
    print("Send message button is not displayed", e)


driver.close()
driver.quit()



