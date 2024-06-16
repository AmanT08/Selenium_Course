import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By




driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
action=ActionChains(driver)
action.move_to_element(driver.find_element(By.CSS_SELECTOR,"#mousehover")).perform()

action.click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.click(driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1")).perform()
action.double_click(driver.find_element(By.CSS_SELECTOR,"#checkBoxOption1")).perform()
time.sleep(2)

# action.click_and_hold()
# action.context_click()
# action.drag_and_drop()
# action.pause()