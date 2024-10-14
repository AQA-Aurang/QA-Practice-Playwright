from playwright.sync_api import Page


def prepare(page: Page):
    page.goto("https://www.qa-practice.com/")
    page.get_by_role("link", name="Single UI Elements").click()
    page.get_by_role("link", name="Iframes").click()


def test_iframe(page: Page):
    prepare(page)
    page.locator("iframe").content_frame.get_by_role("link", name="Visit the homepage").click()
    h1_in_iframe = page.locator("iframe").content_frame.get_by_role("heading", name="Hello!").inner_text()
    assert "Hello!" in h1_in_iframe, "Cannot to interact with iframe"
