import time


def test_set_and_get_cookie(homepage):
    cookie_dict = {'name': 'Test', 'value': 'Test'}
    homepage.cookies.set_cookie(cookie_dict)
    all_cookies = homepage.cookies.get_cookies()
    cookie_names = [cookie['name'] for cookie in all_cookies]
    assert 'example_cookie' in cookie_names


def test_set_and_get_local_storage(homepage):
    homepage.local_storage.set_item('Developer', 'true')
    stored_value = homepage.local_storage.get_item('Developer')
    assert stored_value == 'true'
    time.sleep(30)


def test_remove_local_storage_item(homepage):
    homepage.local_storage.set_item('Developer', 'true')
    homepage.local_storage.remove_item('Developer')
    stored_value = homepage.local_storage.get_item('Developer')
    assert stored_value is None
