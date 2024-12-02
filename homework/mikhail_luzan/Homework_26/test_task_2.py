from playwright.sync_api import Page


def test_fill_in_form(page: Page):
    page.goto('https://demoqa.com/automation-practice-form')

    page.locator('#firstName').fill('Mike')
    page.locator('#lastName').fill('Admin')
    page.locator('#userEmail').fill('test-admin@email.com')
    page.locator('#gender-radio-1 ~ label').click()
    page.locator('#userNumber').fill('1234567890')
    page.locator('#dateOfBirthInput').click()
    page.select_option('select.react-datepicker__month-select', value='11')
    page.select_option('select.react-datepicker__year-select', label='2000')
    days = page.locator('.react-datepicker__day')
    count = days.count()
    for i in range(count):
        if days.nth(i).inner_text() == '31':
            days.nth(i).click()
            break
    subjects = page.locator('#subjectsInput')
    subjects.fill('Computer Science')
    subjects.press('Enter')
    page.locator('#hobbies-checkbox-1 ~ label').check()
    page.locator('#currentAddress').fill('1 Way Street')
    state_dd = page.locator('#react-select-3-input')
    state_dd.fill('Haryana')
    state_dd.press('Enter')
    city_dd = page.locator('#react-select-4-input')
    city_dd.fill('Panipat')
    city_dd.press('Enter')

    page.locator('#submit').click()
