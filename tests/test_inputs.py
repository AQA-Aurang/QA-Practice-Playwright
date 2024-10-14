import pytest
from playwright.sync_api import Page, Locator


def submit(page: Page, locator: Locator):
    locator.focus()
    page.keyboard.press("Enter")


@pytest.mark.usefixtures("chrome_page")
class TestsAlerts:
    DESCRIPTION_TXT = "Cannot fill input field"

    def test_text_input(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Inputs").click()
        input_field = chrome_page.locator("#id_text_string")
        input_field.fill("Something")
        submit(chrome_page, input_field)

        result = chrome_page.locator("#result")
        assert "Something" in result.inner_text(), self.DESCRIPTION_TXT

    @pytest.mark.parametrize("field_name, locator, value", [("Email field", "#id_email", "Faridun@gmail.ru"),
                                                            ("Password field", "#id_password", "Its my secret password - 123")])
    def test_email_and_password_fields(self, chrome_page: Page, field_name: str, locator: str, value: str):
        chrome_page.get_by_role("link", name="Inputs").click()
        chrome_page.get_by_role("link", name=field_name).click()
        input_field = chrome_page.locator(locator)
        input_field.fill(value)
        submit(chrome_page, input_field)

        result = chrome_page.wait_for_selector("#result")
        assert value in result.inner_text(), self.DESCRIPTION_TXT
