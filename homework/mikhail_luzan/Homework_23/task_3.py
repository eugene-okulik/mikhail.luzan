import pytest
import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture()
def driver():
    chrome_driver = webdriver.Chrome()
    yield chrome_driver


def test_choose_language(driver):
    driver.get('https://www.qa-practice.com/elements/select/single_select')

    choose_language = driver.find_element(By.ID, 'id_choose_language')
    dd = Select(choose_language)
    options = dd.options[1:]
    lang_elem = random.choice(options)
    lang_text = lang_elem.text
    dd.select_by_visible_text(lang_text)

    submit_btn = driver.find_element(By.ID, 'submit-id-submit')
    submit_btn.click()

    wait = WebDriverWait(driver, 5)
    result = wait.until(
        EC.visibility_of_element_located((By.ID, 'result'))
    )
    assert lang_text in result.text, f"Expected: '{lang_text}' | Actual: '{result.text}'"


def test_dynamic_loading(driver):
    exp_text = 'Hello World!'
    driver.get('https://the-internet.herokuapp.com/dynamic_loading/2')

    start_btn = driver.find_element(By.CSS_SELECTOR, '#start button')
    start_btn.click()

    wait = WebDriverWait(driver, 10)
    result = wait.until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, '#finish h4'))
    )
    assert exp_text in result.text, f"Expected: '{exp_text}' | Actual: '{result.text}'"
