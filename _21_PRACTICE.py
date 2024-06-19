import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.implicitly_wait(5)
driver.find_element(By.LINK_TEXT,"Shop").click()

names= driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")
Provided_name= "Blackberry"
for name in names:
    if name.find_element(By.CSS_SELECTOR,"h4").text == Provided_name:
        name.find_element(By.CSS_SELECTOR,"button").click()

driver.find_element(By.CSS_SELECTOR,"li[class='nav-item active']").click()

driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()

driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")

wait = WebDriverWait(driver,5)
wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']")))

countries = driver.find_elements(By.CSS_SELECTOR,"div[class='suggestions'] a")


for country in countries:
    if country.text == "India":
        country.click()
        break
driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()

hello = driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
print(hello)

assert "Success" in hello


time.sleep(4)

