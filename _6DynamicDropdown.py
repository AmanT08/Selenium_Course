import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver= webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")

driver.find_element(By.ID,"autosuggest").send_keys("ind")
#li[class="ui-menu-item"] a

time.sleep(1) #because the list takes time yo show

countries= driver.find_elements(By.CSS_SELECTOR, "li[class='ui-menu-item'] a")

print(len(countries))
for country in countries:
    if country.text=='India':
        country.click()
        break

#driver.find_element(By.ID,"autosuggest").text will not work

#USE THIS ONE. JAVASCRIPT DOM
#print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))

assert driver.find_element(By.ID,"autosuggest").get_attribute("value")=='India'
#TO CHECK ID THE VALUE THERE IS RIGHT OR NOT. IF WRONG, ITLL GIVE ASSERTION ERRROR

time.sleep(2)
