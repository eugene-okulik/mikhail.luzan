from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select

url = 'https://demoqa.com/automation-practice-form'

driver = webdriver.Chrome()
driver.set_window_size(3840, 2160)
driver.get(url)

first_name = driver.find_element(By.ID, 'firstName')
first_name.send_keys('Mike')

last_name = driver.find_element(By.ID, 'lastName')
last_name.send_keys('Admin')

email = driver.find_element(By.ID, 'userEmail')
email.send_keys('test-admin@email.com')

gender = driver.find_element(By.CSS_SELECTOR, '#gender-radio-1 ~ label')
gender.click()

mobile = driver.find_element(By.ID, 'userNumber')
mobile.send_keys('1234567890')

birth_date = driver.find_element(By.ID, 'dateOfBirthInput')
birth_date.click()
month_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__month-select')
dropdown = Select(month_select)
dropdown.select_by_value('11')
year_select = driver.find_element(By.CLASS_NAME, 'react-datepicker__year-select')
dropdown = Select(year_select)
dropdown.select_by_value('2000')
days = driver.find_elements(By.CLASS_NAME, 'react-datepicker__day')
for day in days:
    if day.text == "31":
        day.click()
        break

subjects = driver.find_element(By.ID, 'subjectsInput')
subjects.send_keys('Computer Science')
subjects.send_keys(Keys.ENTER)

hobbies = driver.find_element(By.CSS_SELECTOR, '#hobbies-checkbox-1 ~ label')
hobbies.click()

current_address = driver.find_element(By.ID, 'currentAddress')
current_address.send_keys('1 Way Street')

state_dd = driver.find_element(By.ID, "react-select-3-input")
state_dd.send_keys('Haryana')
state_dd.send_keys(Keys.ENTER)

city_dd = driver.find_element(By.ID, "react-select-4-input")
city_dd.send_keys('Panipat')
city_dd.send_keys(Keys.ENTER)

submit_button = driver.find_element(By.ID, 'submit')
submit_button.click()

table = driver.find_element(By.CLASS_NAME, 'table')
print(table.text)
