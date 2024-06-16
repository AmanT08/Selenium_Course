import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# to write into the email box
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")

# to click the check box

driver.find_element(By.ID,"exampleCheck1").click()





time.sleep(5)

