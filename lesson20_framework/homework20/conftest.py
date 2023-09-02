import pytest
from selenium.webdriver import Chrome


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    driver.maximize_window()

    yield driver
    driver.close()