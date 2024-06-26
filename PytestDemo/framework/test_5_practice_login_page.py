from selenium.webdriver.support.select import Select

from baseClass import Base_class
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_6_practice_generalise import GeneralPractice


class TestLoginPage(Base_class):
    def test_practice(self):
        general_obj = GeneralPractice(self.driver)

        general_obj.send_email().send_keys("hello@gmail.com")

        general_obj.click_checkbox().click()

        general_obj.send_name().send_keys("aman")

        # now we can put these two lines in base class
        # because the select option is reusable
        # gender = Select(general_obj.send_Gender())
        # gender.select_by_visible_text("Female")

        self.MethodForSelect(general_obj.send_Gender(),"Female")

        general_obj.click_submit().click()

        message = general_obj.alert_message().text
        print(message)

        assert "Success!" in message

