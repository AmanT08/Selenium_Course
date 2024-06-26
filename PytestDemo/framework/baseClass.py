import pytest
from selenium.webdriver.support.select import Select


@pytest.mark.usefixtures("general_Browser")
class Base_class():

    def MethodForSelect(self,locator,text):
        gender = Select(locator)
        gender.select_by_visible_text(text)

