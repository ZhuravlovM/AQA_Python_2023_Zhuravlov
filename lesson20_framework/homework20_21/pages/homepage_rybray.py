from lesson20_framework.homework20_21.pages.base_page_rybray import BasePageRybray


class HomePageRybray(BasePageRybray):

    def __init__(self, driver):
        super().__init__(driver)
        # for homework of lesson 20
        self.__spinning_page_locator = ('xpath', '//a[@id="ui-id-41"]')
        self.__feeder_page_locator = ('xpath', '//a[@id="ui-id-43"]')
        self.__catalogue_locator = ('xpath', '//div[@class="categories-button"]')
        self.__compare_items_locator = ('xpath', '//a[@class="link-to-compare"]')
        self.__new_arrivals_locator = ('xpath', '//a[@href="/uk/novynky/"]')

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
