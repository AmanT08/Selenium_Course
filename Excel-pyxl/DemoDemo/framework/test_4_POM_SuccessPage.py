from selenium.webdriver.common.by import By


class Success:

    def __init__(self,driver):
        self.driver = driver

    send_country_name = (By.CSS_SELECTOR,"#country")

    wait_till = (By.XPATH,"//div[@class='suggestions']")

    country_names = (By.CSS_SELECTOR,"div[class='suggestions'] a")

    term_condition_checkbox = (By.CSS_SELECTOR,".checkbox.checkbox-primary")

    submit_button = (By.XPATH,"//input[@type='submit']")

    message_printed = (By.CSS_SELECTOR,".alert.alert-success.alert-dismissible")

    def send_country(self):
        return self.driver.find_element(*Success.send_country_name)

    def wait_condition(self):
        return Success.wait_till

    def get_country_names(self):
        return self.driver.find_elements(*Success.country_names)

    def termsConditon_checkbox(self):
        return self.driver.find_element(*Success.term_condition_checkbox)

    def submit_order(self):
        return self.driver.find_element(*Success.submit_button)

    def success_message(self):
        return self.driver.find_element(*Success.message_printed)
