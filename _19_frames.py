import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.implicitly_wait(5)

driver.switch_to.frame("courses-iframe")

print(driver.find_element(By.XPATH,"(//div[@class='login-btn'])[1]").text)

# to switch back
driver.switch_to.default_content()
print(driver.find_element(By.XPATH,"//legend[normalize-space()='iFrame Example']").text)