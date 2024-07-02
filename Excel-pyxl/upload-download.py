import time
import openpyxl
from fun_excel_upload import to_update_excel
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

file_path= "C:/Users/hp/Downloads/download.xlsx"
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.implicitly_wait(5)

driver.find_element(By.ID, "downloadButton").click()
fruit_name = "Apple"
new_value="500"
# to get the price before uploading
original_price= driver.find_element(By.XPATH,
                                    "//div[text()='"+fruit_name+
                                    "']/parent::div/parent::div//div[@id='cell-4-undefined']/div").text
print(original_price)

# now edit the excel
to_update_excel(file_path, fruit_name, new_value)

# to upload the file, it should have type=file in HTML, if not ask developer
file=driver.find_element(By.CSS_SELECTOR,"input[type='file']")
file.send_keys(file_path)
time.sleep(3)


# wait for the alert message
wait=WebDriverWait(driver,5)
wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")))

#to check the price after uploading
After_upload_price= driver.find_element(By.XPATH,
                                        "//div[text()='"+fruit_name+
                                        "']/parent::div/parent::div//div[@id='cell-4-undefined']/div").text
assert After_upload_price == new_value







