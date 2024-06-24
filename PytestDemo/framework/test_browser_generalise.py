import time
from framework.baseClass import Base_class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class TestClassFramework(Base_class):

    def test_method_website(self):
        self.driver.find_element(By.LINK_TEXT,"Shop").click()

        names= self.driver.find_elements(By.CSS_SELECTOR,"div[class='card h-100']")
        provided_name= "Blackberry"
        for name in names:
            if name.find_element(By.CSS_SELECTOR,"h4").text == provided_name:
                name.find_element(By.CSS_SELECTOR,"button").click()

        self.driver.find_element(By.CSS_SELECTOR,"li[class='nav-item active']").click()

        self.driver.find_element(By.CSS_SELECTOR,"button[class='btn btn-success']").click()

        self.driver.find_element(By.CSS_SELECTOR,"#country").send_keys("Ind")

        wait = WebDriverWait(self.driver,5)
        wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']")))

        countries = self.driver.find_elements(By.CSS_SELECTOR,"div[class='suggestions'] a")

        for country in countries:
            if country.text == "India":
                country.click()
                break
        self.driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()
        self.driver.find_element(By.XPATH,"//input[@type='submit']").click()

        hello = self.driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
        print(hello)

        assert "Success" in hello
