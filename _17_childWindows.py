import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
time.sleep(2)
driver.find_element(By.LINK_TEXT,"Click Here").click()
time.sleep(2)
# to generate list of handles of windows opened, used for switching
window_Opened= driver.window_handles

# to switch
driver.switch_to.window(window_Opened[1])

# to print text of child window
print(driver.find_element(By.XPATH,"//h3").text)
# now we don't need the child window anymore so we will close it
driver.close()
time.sleep(1)
# switch back to parent
driver.switch_to.window(window_Opened[0])

print(driver.find_element(By.XPATH,"//h3").text)

