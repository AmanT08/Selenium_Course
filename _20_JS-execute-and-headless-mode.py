import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# to run in HEADLESS MODE- test will run in background

chrome_opt= webdriver.ChromeOptions()
chrome_opt.add_argument("headless")

# to ignore the certification errors in browser
# like your connection is not private
chrome_opt.add_argument("--ignore-certificate-errors")


driver=webdriver.Chrome(options=chrome_opt)
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

driver.execute_script("window.scroll(0,500);")

# to take a ss
driver.get_screenshot_as_file("screen.png")