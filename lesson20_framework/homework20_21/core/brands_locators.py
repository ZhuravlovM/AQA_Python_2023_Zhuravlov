from lesson20_framework.homework20_21.core.base_locators_rybray import BaseLocatorsRybray


class BrandsLocators(BaseLocatorsRybray):
    def __init__(self):
        super().__init__()
        self.search_field_brands = ('xpath', '//input[@class="input-text ambrands-input"]')
        self.search_button_all_brands = ('xpath', '//button[@class="ambrands-letter -letter-all -active"')
        self.search_result_sub_header = ('xpath', '//li[@class="item all-products"]')
        self.search_brand_daiwa = ('xpath', '//a[@href="https://rybray.com.ua/uk/brendy/daiwa"]')
        self.search_button_a = ('xpath', '//button[@class="ambrands-letter letter-A"]')
        self.search_button_b = ('xpath', '//button[@class="ambrands-letter letter-B"]')
        self.search_button_a_result = ('xpath', '//div[@class="ambrands-letter letter-A am-brands-fullwidth"]')
        self.brand_abu_garcia = ('xpath', '//a[@title="ABU GARCIA"]')
        self.brand_garmin = ('xpath', '//a[@title="GARMIN"]')
        self.brand_rapala = ('xpath', '//a[@title="RAPALA"]')
