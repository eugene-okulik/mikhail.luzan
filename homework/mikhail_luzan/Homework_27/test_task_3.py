from playwright.sync_api import Page


def test_red_button(page: Page):
    page.goto('https://demoqa.com/dynamic-properties')
    page.locator('.text-danger').click()
