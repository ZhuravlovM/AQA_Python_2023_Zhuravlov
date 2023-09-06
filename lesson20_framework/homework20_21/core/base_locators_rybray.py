

class BaseLocatorsRybray:
    def __init__(self):
        self.logo = ('xpath', '//span[@class="logo"]')
        self.search = ('xpath', '//input[@id="search"]')
        self.search_button = ('xpath', '//button[@class="action search"]')
        self.search_result_sub_header = ('xpath', '//li[@class="item search"]')
        self.wishlist = ('xpath', '//div[@class="link wishlist"]')
        self.user_cabinet = ('xpath', '//div[@class="user-cabinet"]')
        self.brands_page = ('xpath', '//a[@id="ui-id-58"]')
