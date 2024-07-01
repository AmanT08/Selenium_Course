from selenium.webdriver.common.by import By

from test_4_POM_SuccessPage import Success


class ShopPage:
    def __init__(self,driver):
        self.driver = driver

    model_names = (By.CSS_SELECTOR,"div[class='card h-100']")

    name_in_list = (By.CSS_SELECTOR,"h4")

    add_to_checkout = (By.CSS_SELECTOR,"button")

    Checkout_button = (By.CSS_SELECTOR,"li[class='nav-item active']")

    confirm_button = (By.CSS_SELECTOR,"button[class='btn btn-success']")
    def get_model_names(self):
        return self.driver.find_elements(*ShopPage.model_names)

    def get_actual_name(self,name):
        return name.find_element(*ShopPage.name_in_list)

    def add_item_button(self,name):
        return name.find_element(*ShopPage.add_to_checkout)

    def checkout(self):
        return self.driver.find_element(*ShopPage.Checkout_button)

    def confirm(self):
        self.driver.find_element(*ShopPage.confirm_button).click()

        success_obj = Success(self.driver)
        return success_obj
