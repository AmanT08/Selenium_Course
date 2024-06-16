import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#input[type='radio']

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.find_element(By.CSS_SELECTOR,"#name").send_keys("aman")

# now click the  alert button
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()

# now switch to alert mode
alert = driver.switch_to.alert

# to get the text in alert
print(alert.text)

# to check if name is in alert
assert "aman" in alert.text

# to click on the ok in alert
alert.accept()

# alert.decline()  if there is a cancel button




time.sleep(2)
