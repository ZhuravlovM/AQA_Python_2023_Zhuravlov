import pytest
from selenium.webdriver import Chrome
from lesson20_framework.homework20_21.pages.homepage_rybray import HomePageRybray
from lesson20_framework.homework20_21.pages.brands_page import BrandsPageRybray


@pytest.fixture(scope='session')
def driver():
    driver = Chrome()
    driver.maximize_window()

    yield driver
    driver.close()


@pytest.fixture
def homepage(driver):
    driver.get('https://rybray.com.ua/uk/')
    yield HomePageRybray(driver)


@pytest.fixture
def brandspage(driver):
    driver.get('https://rybray.com.ua/uk/brendy/')
    yield BrandsPageRybray(driver)
