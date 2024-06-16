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

# now to add the total price shown
total = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
print(len(total))
sum=0
for price in total:
    sum+= int(price.text)
print(sum)

total_amount = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert sum==total_amount


driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")


# NOW INSTEAD OF USING SLEEP WE USE implicitly_wait() under chrome

# so even if button takes time to load the next line, wait will be there

# but let's assume it takes more than the time provided in implicit wait
# , so we give explicit wait only limited to that item
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()

wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))

text_shown = driver.find_element(By.CSS_SELECTOR,".promoInfo").text
assert "Code applied" in text_shown

# to check that discount amount is less than the total amount calculated above
discount = int(float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text))
assert discount < total_amount