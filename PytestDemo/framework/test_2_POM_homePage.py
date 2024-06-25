from selenium.webdriver.common.by import By


class TestHomePage:

    def __init__(self,driver):
        self.driver = driver

    shop= ((By.LINK_TEXT,"Shop"))

    def test_home_page(self):
        return self.driver.find_element(*TestHomePage.shop)
