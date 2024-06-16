import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ber")
time.sleep(3)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")

counts = len(results)
assert counts > 0

for items in results:
    items.find_element(By.XPATH, "div/button").click()
time.sleep(2)

driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
time.sleep(1)

#  //div[@class='action-block']/button
# //button[text()='proceed to checkout'  can use the text on button

driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()

time.sleep(2)

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
time.sleep(2)

# NOW WE DONT USE TIME.SLEEP() AGAIN AND AGAIN, WE NEED TO USE IMPLICIT OR EXPLICIT WAITS







