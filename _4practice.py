import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get('https://rahulshettyacademy.com/client')

# to get the link on the page
driver.find_element(By.LINK_TEXT,"Forgot password?").click()

# to write the email using parent child traversing by Xpath- //form/div/input
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("abc8611@gmail.com")

# to write password using css selector with parent child traverse:- form div:nth-child(2) input
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@123")

# to write confirm password
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@123")

# to click on submit using the text of the button
# driver.find_element(By.XPATH,"//button[@type='submit']").click()
driver.find_element(By.XPATH,"//button[text()='Save New Password']").click()





time.sleep(5)