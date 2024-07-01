from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class GeneralPractice:
    def __init__(self,driver):
        self.driver= driver

    Email = (By.NAME, "email")
    CheckBox = (By.ID, "exampleCheck1")
    Name = (By.CSS_SELECTOR, "input[name='name']")
    Gender = (By.ID, "exampleFormControlSelect1")
    Submit = (By.XPATH, "//input[@type='submit']")
    Alert = (By.CLASS_NAME, "alert")

    def send_email(self):
        return self.driver.find_element(*GeneralPractice.Email)

    def click_checkbox(self):
        return self.driver.find_element(*GeneralPractice.CheckBox)

    def send_name(self):
        return self.driver.find_element(*GeneralPractice.Name)

    def send_Gender(self):
        return self.driver.find_element(*GeneralPractice.Gender)

    def click_submit(self):
        return self.driver.find_element(*GeneralPractice.Submit)

    def alert_message(self):
        return self.driver.find_element(*GeneralPractice.Alert)




