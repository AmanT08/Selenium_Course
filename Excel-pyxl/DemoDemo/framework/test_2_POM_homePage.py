from selenium.webdriver.common.by import By

from test_3_POM_ShopPage import ShopPage


class TestHomePage:

    def __init__(self,driver):
        self.driver = driver

    shop= ((By.LINK_TEXT,"Shop"))

    def test_home_page(self):
        self.driver.find_element(*TestHomePage.shop).click()
        shop_obj = ShopPage(self.driver)
        return shop_obj

