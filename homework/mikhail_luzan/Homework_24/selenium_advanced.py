import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver


def test_cart(driver):
    driver.get('https://www.demoblaze.com/index.html')

    wait = WebDriverWait(driver, 10)
    links = wait.until(
        EC.visibility_of_all_elements_located((By.CSS_SELECTOR, '.card-title a'))
    )

    link = random.choice(links)
    link_txt = link.text
    actions = ActionChains(driver)
    actions.key_down(Keys.CONTROL).click(link).key_up(Keys.CONTROL).perform()

    tabs = driver.window_handles
    driver.switch_to.window(tabs[1])

    add_btn = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#tbodyid .btn-success'))
    )
    add_btn.click()
    wait.until(EC.alert_is_present())
    alert = Alert(driver)
    alert.accept()

    driver.close()
    driver.switch_to.window(tabs[0])
    driver.find_element(By.ID, 'cartur').click()

    cart_item = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'tr[class="success"]'))
    )
    assert link_txt in cart_item.text, f"Expected: '{link_txt}' | Actual: '{cart_item.text}'"


def test_compare_products(driver):
    driver.get('https://magento.softwaretestingboard.com/gear/bags.html')

    wait = WebDriverWait(driver, 10)
    item = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '.product-item-info a[class=product-item-link]'))
    )
    item_txt = item.text
    compare_btn = driver.find_element(By.CSS_SELECTOR, 'a[class="action tocompare"]')

    actions = ActionChains(driver)
    actions.move_to_element(item)
    actions.click(compare_btn)
    actions.perform()

    compare = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#compare-items a[class=product-item-link]'))
    )
    compare_txt = compare.text
    assert item_txt == compare_txt, f"Expected: '{item_txt}' | Actual: '{compare_txt}"
