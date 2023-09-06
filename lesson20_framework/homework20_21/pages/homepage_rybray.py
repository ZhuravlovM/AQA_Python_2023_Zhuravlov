from lesson20_framework.homework20_21.pages.base_page_rybray import BasePageRybray
from lesson20_framework.homework20_21.core.base_locators_rybray import BaseLocatorsRybray
from lesson20_framework.homework20_21.pages.brands_page import BrandsPageRybray


class HomePageRybray(BasePageRybray):

    def __init__(self, driver):
        super().__init__(driver)
        self.locators = BaseLocatorsRybray()

# For homework of lesson 20

    def go_to_spinning_page(self):
        locator = ('xpath', '//a[@id="ui-id-41"]')
        element = self.wait_for_element(locator)
        element.click()

    def go_to_feeder_page(self):
        locator = ('xpath', '//a[@id="ui-id-43"]')
        element = self.wait_for_element(locator)
        element.click()

    def open_catalog(self):
        locator = ('xpath', '//div[@class="categories-button"]')
        element = self.wait_for_element(locator)
        element.click()

    def go_to_items_comparison(self):
        locator = ('xpath', '//a[@class="link-to-compare"]')
        element = self.wait_for_element(locator)
        element.click()

    def go_to_new_arrivals(self):
        locator = ('xpath', '//a[@href="/uk/novynky/"]')
        element = self.wait_for_element(locator)
        element.click()

# For homework of lesson 21

    def go_to_brands_page(self):
        self.click_element(self.locators.brands_page)
        return BrandsPageRybray(self._driver)

    def use_search_field(self, text):
        self.send_keys(self.locators.search, text)
        self.click_element(self.locators.search_button)

    def open_wishlist(self):
        self.click_element(self.locators.wishlist)