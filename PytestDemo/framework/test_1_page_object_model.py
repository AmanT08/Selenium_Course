import time
from baseClass import Base_class
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from test_2_POM_homePage import TestHomePage
from test_3_POM_ShopPage import ShopPage
from test_4_POM_SuccessPage import Success


class TestClassFramework(Base_class):

    def test_method_website(self):
        home_p= TestHomePage(self.driver)

        # made the shop object in home file and then passed it here
        shop_p = home_p.test_home_page()

        names= shop_p.get_model_names()
        provided_name= "Blackberry"

        for name in names:
            name_of_item = shop_p.get_actual_name(name).text
            if name_of_item == provided_name:
                shop_p.add_item_button(name).click()

        shop_p.checkout().click()

       # made the object in shop file
        success_obj = shop_p.confirm()

        success_obj.send_country().send_keys("Ind")

        wait = WebDriverWait(self.driver,5)
        wait.until((expected_conditions.presence_of_element_located(success_obj.wait_condition())))
        # wait.until(expected_conditions.presence_of_element_located((By.XPATH,"//div[@class='suggestions']")))

        countries = success_obj.get_country_names()

        for country in countries:
            if country.text == "India":
                country.click()
                break

        # self.driver.find_element(By.CSS_SELECTOR,".checkbox.checkbox-primary").click()

        success_obj.termsConditon_checkbox().click()

        # self.driver.find_element(By.XPATH,"//input[@type='submit']").click()

        success_obj.submit_order().click()

        # message = self.driver.find_element(By.CSS_SELECTOR,".alert.alert-success.alert-dismissible").text
        message = success_obj.success_message().text

        assert "Success" in message
