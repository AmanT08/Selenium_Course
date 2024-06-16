import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")

driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()

newWindows=driver.window_handles
driver.switch_to.window(newWindows[1])

text1 = driver.find_element(By.CSS_SELECTOR,".im-para.red").text
print(text1)
sp=text1.split()
mail=""
for i in sp:
    if ".com" in i:
        mail=i
        break
print(mail)
driver.close()
driver.switch_to.window(newWindows[0])

driver.find_element(By.ID,"username").send_keys(mail)
driver.find_element(By.ID,"password").send_keys("abcd1234")


driver.find_element(By.CSS_SELECTOR,"#terms").click()

driver.find_element(By.CSS_SELECTOR,"#signInBtn").click()


wait = WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".alert-danger")))
print(driver.find_element(By.CSS_SELECTOR,".alert-danger").text)