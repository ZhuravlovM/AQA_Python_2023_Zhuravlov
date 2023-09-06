import time


# Tests for homework of lesson 20
def test_go_to_spinning_page(homepage):
    homepage.go_to_spinning_page()
    time.sleep(5)


def test_go_to_feeder_page(homepage):
    homepage.go_to_feeder_page()
    time.sleep(5)


def test_open_catalog(homepage):
    homepage.open_catalog()
    time.sleep(5)


def test_go_to_items_comparison(homepage):
    homepage.go_to_items_comparison()
    time.sleep(5)


def test_go_to_new_arrivals(homepage):
    homepage.go_to_new_arrivals()
    time.sleep(5)


# Tests for homework of lesson 21
def test_go_to_brands_page(homepage):
    homepage.go_to_brands_page()
    time.sleep(5)


def test_use_search_field(homepage):
    homepage.use_search_field('котушка')
    homepage.wait_for_element(homepage.locators.search_result_sub_header)
    sub_header = homepage.check_element(homepage.locators.search_result_sub_header)
    assert sub_header.text == "Результати пошуку: 'котушка'"


def test_open_wishlist(homepage):
    homepage.open_wishlist()
    time.sleep(5)
