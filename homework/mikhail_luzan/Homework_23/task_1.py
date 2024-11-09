from selenium import webdriver
from selenium.webdriver.common.by import By


url = 'https://www.qa-practice.com/elements/input/simple'
text = 'someTHing'

driver = webdriver.Chrome()
driver.get(url)

text_input = driver.find_element(By.ID, 'id_text_string')
text_input.send_keys(text)
text_input.submit()

text_output = driver.find_element(By.ID, 'result-text')
print(text_output.text)
