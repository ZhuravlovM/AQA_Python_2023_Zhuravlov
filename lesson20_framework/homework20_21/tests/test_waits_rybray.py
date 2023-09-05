from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_01():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    search_field_locator = "//input[@id='search']"
    driver.implicitly_wait(5)
    element = driver.find_element(by='xpath', value=search_field_locator)
    element.send_keys('Котушка Ryobi')
    action = ActionChains(driver)
    action.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
    action.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()


def test_02():
    driver = Chrome()
    driver.get('https://rybray.com.ua/uk/')
    web_driver_wait = WebDriverWait(driver, 3)
    search_input_locator = '//input[@placeholder="Пошук в каталозі товарів"]'
    search_input_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_input_locator,)))
    search_input_with_wait.send_keys('Котушка')
    search_first_result_locator = '//div[@class="title"]/a'
    search_first_result_with_wait = web_driver_wait.until(EC.presence_of_element_located(('xpath', search_first_result_locator,)))
    assert search_first_result_with_wait.get_attribute('href') == 'https://rybray.com.ua/uk/kotushka-teben-teb/'

