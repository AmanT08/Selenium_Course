import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

boxes=driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(boxes))

for box in boxes:
    if box.get_attribute("value") == "option2":
        box.click()
        assert box.is_selected()
        break
time.sleep(3)

