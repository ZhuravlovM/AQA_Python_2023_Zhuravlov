import time


def test_go_to_abu_garcia_brand(homepage):
    brands_page = homepage.go_to_brands_page()
    abu_garcia_page = brands_page.go_to_abu_garcia_brand()
    time.sleep(5)


def test_sort_brands_by_a(homepage):
    brands_page = homepage.go_to_brands_page()
    brands_page.sort_brands_by_a()
    time.sleep(5)


def test_use_brands_search(brandspage):
    brandspage.use_brands_search('Daiwa')
    sub_header = brandspage.check_element(brandspage.locators.search_result_sub_header)
    assert sub_header.text == "DAIWA"
