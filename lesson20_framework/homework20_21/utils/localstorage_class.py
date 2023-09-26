

class LocalStorage:
    def __init__(self, driver):
        self._driver = driver

    def set_item(self, key, value):
        script = f"localStorage.setItem('{key}', '{value}')"
        self._driver.execute_script(script)

    def get_item(self, key):
        script = f"return localStorage.getItem('{key}')"
        return self._driver.execute_script(script)

    def remove_item(self, key):
        script = f"localStorage.removeItem('{key}')"
        self._driver.execute_script(script)

    def clear(self):
        script = "localStorage.clear()"
        self._driver.execute_script(script)
