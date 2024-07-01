import pytest
from selenium.webdriver.support.select import Select

from baseClass import Base_class
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from test_6_practice_generalise import GeneralPractice


class TestLoginPage(Base_class):
    def test_practice(self,dynamic_data):
        general_obj = GeneralPractice(self.driver)

        # now see we are passing hard coded values to test
        # what if we want to make it dynamic
        # so, we write fixture
        # in same file as test, not on conftest file

        general_obj.send_email().send_keys(dynamic_data[0])

        general_obj.click_checkbox().click()

        general_obj.send_name().send_keys(dynamic_data[1])

        self.MethodForSelect(general_obj.send_Gender(),dynamic_data[2])

        general_obj.click_submit().click()

        message = general_obj.alert_message().text
        print(message)

        assert "Success!" in message

        self.driver.refresh()
        time.sleep(3)

    @pytest.fixture(params=(("hello@h=gmail.com","aman","Male"),("abcd@gmail.com","abcd","Female")))
    def dynamic_data(self,request):
        return request.param

