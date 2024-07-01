import pytest
from selenium.webdriver.support.select import Select


from DemoDemo.framework.baseClass import Base_class
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

from DemoDemo.framework.test_6_practice_generalise import GeneralPractice
from data_for_test import DataForTest


class TestLoginPage(Base_class):
    def test_practice(self,dynamic_data):
        general_obj = GeneralPractice(self.driver)

        # now see we are passing hard coded values to test
        # what if we want to make it dynamic
        # so, we write fixture
        # in same file as test, not on conftest file

        general_obj.send_email().send_keys(dynamic_data["Email"])

        general_obj.click_checkbox().click()

        general_obj.send_name().send_keys(dynamic_data["name"])

        self.MethodForSelect(general_obj.send_Gender(),dynamic_data["gender"])

        general_obj.click_submit().click()

        message = general_obj.alert_message().text
        print(message)

        assert "Success!" in message

        self.driver.refresh()
        time.sleep(3)

    # now instead of using tuple, we use dictionary to make it more readable

    # you can make another file for the data and the just pass the value in params

    @pytest.fixture(params=DataForTest.dataa("t2"))
    def dynamic_data(self,request):
        return request.param

