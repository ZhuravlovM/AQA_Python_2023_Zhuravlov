from lesson20_framework.homework20_21.pages.base_page_rybray import BasePageRybray
from lesson20_framework.homework20_21.pages.brand_abu_garcia_page import AbuGarciaPage
from lesson20_framework.homework20_21.core.brands_locators import BrandsLocators


class BrandsPageRybray(BasePageRybray):
    def __init__(self, driver):
        super().__init__(driver)
        self.locators = BrandsLocators()

    def go_to_abu_garcia_brand(self):
        self.click_element(self.locators.brand_abu_garcia)
        return AbuGarciaPage(self._driver)

    def use_brands_search(self, text):
        self.send_keys(self.locators.search_field_brands, text)
        self.click_element(self.locators.search_brand_daiwa)

    def sort_brands_by_a(self):
        self.click_element(self.locators.search_button_a)
        self.check_element(self.locators.search_button_a_result)
