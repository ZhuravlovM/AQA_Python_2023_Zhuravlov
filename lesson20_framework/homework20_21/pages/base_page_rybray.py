from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePageRybray:

    def __init__(self, driver):
        self._driver = driver
        self.__web_driver_wait = WebDriverWait(self._driver, 10)

    def wait_for_element(self, locator):
        return self.__web_driver_wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        self.wait_for_element(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    def press_enter(self, locator):
        self.wait_for_element(locator).send.keys(Keys.ENTER)

    def refresh_page(self):
        self._driver.refresh()
        