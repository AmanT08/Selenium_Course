import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

# implicit wait gives max of 5 seconds to every object to load
# if it loads immediately, it'll not wait 5 seconds unlike time.sleep()
driver.implicitly_wait(5)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")

list1=["Capsicum","Apple - 1 Kg","Grapes - 1 Kg"]

driver.find_element(By.CSS_SELECTOR, ".search-keyword").send_keys("ap")
time.sleep(3)
list3=[]
list2 = driver.find_elements(By.CSS_SELECTOR,"div[class='product'] h4")
for i in list2:
    list3.append(i.text)
print(list3)
assert list1==list3


