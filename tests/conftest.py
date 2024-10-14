import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="class")
def chrome_page(request):
    # """Returns chrome page temporary"""
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)   # firefox / webkit
        page = browser.new_page()
        page.goto("https://www.qa-practice.com/")
        page.get_by_role("link", name="Single UI Elements").click()
        request.cls.driver = page

        yield page

        browser.close()
