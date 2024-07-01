import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def general_Browser(request):
    driver = webdriver.Chrome()
    driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.implicitly_wait(5)
    driver.maximize_window()
    request.cls.driver = driver

    yield
    driver.close()
