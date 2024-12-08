from playwright.sync_api import Page, expect, Route
import re
import json


def test_iphone_title(page: Page):

    _TEXT_TO_REPLACE = 'яблокофон 16 про'

    def handle_route(route: Route):
        resp = route.fetch()
        body = resp.json()
        body['body']['digitalMat'][0]['familyTypes'][0]['productName'] = _TEXT_TO_REPLACE
        body = json.dumps(body)
        route.fulfill(
            response=resp,
            body=body
        )

    page.route(re.compile('/api/digital-mat'), handle_route)
    page.goto('https://www.apple.com/shop/buy-iphone')
    page.locator('(//*[contains(@class, "rf-hcard rf-hcard-40")])[1]').click()
    title = page.locator('(//*[@id="rf-digitalmat-overlay-label-0"])[1]')
    expect(title).to_have_text(_TEXT_TO_REPLACE)
