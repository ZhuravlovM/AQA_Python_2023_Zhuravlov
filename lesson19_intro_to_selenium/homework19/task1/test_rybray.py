from selenium.webdriver import Chrome
import time


def test_search():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    search_field_locator = "//input[@id='search']"
    search_field = driver.find_element(by='xpath', value=search_field_locator)
    search_field.send_keys('Котушка')
    search_button_locator = "//button[@class='action search']"
    search_button = driver.find_element(by='xpath', value=search_button_locator)
    search_button.click()
    time.sleep(5)


def test_open_catalogue():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    catalogue_locator = "//div[@class='categories-button']"
    catalogue = driver.find_element(by='xpath', value=catalogue_locator)
    catalogue.click()
    time.sleep(5)


def test_subscription():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    subscription_field_locator = "//input[@id='newsletter']"
    subscription_field = driver.find_element(by='xpath', value=subscription_field_locator)
    subscription_field.send_keys('testmail@gmail.com')
    subscribe_button_locator = "//button[@class='action subscribe primary']"
    subscribe_button = driver.find_element(by='xpath', value=subscribe_button_locator)
    subscribe_button.click()
    time.sleep(5)


def test_empty_cart_message():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    cart_locator = ".showcart"
    cart = driver.find_element(by='css selector', value=cart_locator)
    time.sleep(5)
    cart.click()
    empty_cart_text_locator = "strong.subtitle.empty"
    empty_cart_text = driver.find_element(by='css selector', value=empty_cart_text_locator)
    expected_text = "У вас немає товарів в кошику."
    actual_text = empty_cart_text.text
    assert actual_text == expected_text, "Текст не відповідає умовам"


def test_catalogue_pdf():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    catalogue_pdf_locator = ".download-catalog-link a"
    catalogue_pdf = driver.find_element(by='css selector', value=catalogue_pdf_locator)
    catalogue_pdf_url = catalogue_pdf.get_attribute('href')
    time.sleep(2)
    catalogue_pdf.click()
    time.sleep(5)
    expected_url = "https://rybray.com.ua/uk/media/wysiwyg/10.04.23_Catalogue.pdf"
    assert catalogue_pdf_url == expected_url, "Адреса сторінки не відповідає очікуванній"
