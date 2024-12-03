from playwright.sync_api import Page


def test_login(page: Page):
    page.goto('https://the-internet.herokuapp.com/')
    page.get_by_role('link', name='Form Authentication').click()
    username = page.get_by_role('textbox', name='Username')
    password = page.get_by_role('textbox', name='Password')
    username.fill('tomsmith')
    password.fill('SuperSecretPassword!')
    page.get_by_role('button').click()
