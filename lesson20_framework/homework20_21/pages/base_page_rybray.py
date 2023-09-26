from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from lesson20_framework.homework20_21.utils.cookies_class import Cookies
from lesson20_framework.homework20_21.utils.localstorage_class import LocalStorage


class BasePageRybray:

    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)
        self.cookies = Cookies(self._driver)
        self.local_storage = LocalStorage(self._driver)

    def wait_for_element(self, locator):
        return self.__web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    def press_enter(self, locator):
        self.wait_for_element(locator).send_keys(Keys.ENTER)

    def refresh_page(self):
        self._driver.refresh()

    def check_element(self, locator):
        return self._driver.find_element(*locator)
        