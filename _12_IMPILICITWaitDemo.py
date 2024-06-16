import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# implicit wait gives max of 5 seconds to every object to load
# if it loads immediately, it'll not wait 5 seconds unlike time.sleep()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ap")
time.sleep(3)
action = driver.find_elements(By.CSS_SELECTOR,".product-action")
for value in action:
    value.click()
time.sleep(3)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(1)

#  //div[@class='action-block']/button
# //button[text()='proceed to checkout'  can use the text on button

driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

# NOW INSTEAD OF USING SLEEP WE USE implicitly_wait() under chrome

# so even if button takes time to load the next line, wait will be there
text_shown = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert "code applied" in text_shown







