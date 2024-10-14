import pytest
from playwright.sync_api import Page, Locator, Dialog, ElementHandle


def click_by_mouse(page: Page, locator: Locator | ElementHandle, x: int, y: int):
    locator.focus()
    page.mouse.click(x, y)


def work_with_alerts(alert: Dialog):
    if alert.type == "alert":
        alert.accept()
    elif alert.type == "confirm":
        alert.dismiss()
    else:
        alert.accept("Hello world!")


@pytest.mark.usefixtures("chrome_page")
class TestsAlerts:

    def test_alert_box(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Alerts").click()
        chrome_page.on("dialog", work_with_alerts)
        # chrome_page.once("dialog", work_with_alerts)
        chrome_page.get_by_role("link", name="Click").click()

    @pytest.mark.parametrize("link_name, expected", [("Confirmation box", "Cancel"), ("Prompt box", "Hello world")])
    def test_confirmation_and_prompt_box(self, chrome_page: Page, link_name: str, expected: str):
        chrome_page.get_by_role("link", name="Alerts").click()
        chrome_page.get_by_role("link", name=link_name).click()
        chrome_page.on("dialog", work_with_alerts)
        # chrome_page.once("dialog", work_with_alerts)
        chrome_page.get_by_role("link", name="Click").click()

        actual = chrome_page.locator("#result").inner_text().strip()
        assert expected in actual, "Cannot to interact with confirmation alert"
