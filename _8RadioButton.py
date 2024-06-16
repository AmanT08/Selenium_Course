import time
from selenium import webdriver
from selenium.webdriver.common.by import By


#input[type='radio']

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

boxes=driver.find_elements(By.CSS_SELECTOR, "input[type='radio']")
print(len(boxes))

for box in boxes:
    if box.get_attribute("value") == "radio3":
        box.click()
        assert box.is_selected()
        break
# But if the position will not change everytime then    directly put
# boxes[2].click instead of using for loop


# HIDDEN TEXT
# TO CHECK IF IT IS SHOWING WHEN WE OPEN THE BROWSER
assert driver.find_element(By.ID, "displayed-text").is_displayed()

# NOW CLICK THE BUTTON TO HIDE IT
driver.find_element(By.ID, "hide-textbox").click()

# NOW TO CHECK IF IT GOT HIDDEN by using not
assert not driver.find_element(By.ID, "displayed-text").is_displayed()


time.sleep(5)