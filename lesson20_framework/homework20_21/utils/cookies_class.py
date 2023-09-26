

class Cookies:
    def __init__(self, driver):
        self._driver = driver

    def set_cookie(self, cookie_dict):
        self._driver.add_cookie(cookie_dict)

    def get_cookies(self):
        return self._driver.get_cookies()