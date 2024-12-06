from playwright.sync_api import Page, expect, BrowserContext


def test_tabs(page: Page, context: BrowserContext):
    page.goto('https://www.qa-practice.com/elements/new_tab/button')
    click_btn = page.locator('#new-page-button')
    with context.expect_page() as new_page_event:
        click_btn.click()
    new_page = new_page_event.value
    result = new_page.locator('#result-text')
    expect(result).to_have_text('I am a new page in a new tab')
    expect(click_btn).to_be_enabled()
