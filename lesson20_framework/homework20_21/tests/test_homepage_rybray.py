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
