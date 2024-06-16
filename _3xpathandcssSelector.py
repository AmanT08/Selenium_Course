import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()

driver.get("https://rahulshettyacademy.com/angularpractice/")

# to write into the email box
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")

# to click the check box

driver.find_element(By.ID,"exampleCheck1").click()


# css selector tagname[attribute='value']
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("aman")

# xpath //tagname[@attribute="value"]
driver.find_element(By.XPATH,"//input[@type='submit']").click()

# to print a text
message = driver.find_element(By.CLASS_NAME,"alert").text
print(message)

# to check if we got the right mesage we use assertion
assert "Success!" in message





time.sleep(5)