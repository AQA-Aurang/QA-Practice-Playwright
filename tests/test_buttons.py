import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsButtons:
    ACTUAL_RESULT = "Submitted"
    DESCRIPTION_TXT = "Cannot push on button"

    def test_simple_button(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Buttons").click()
        chrome_page.get_by_role("button", name="Click").click()

        expected_result = chrome_page.locator("#result").text_content().strip()
        assert self.ACTUAL_RESULT == expected_result, self.DESCRIPTION_TXT

    def test_looks_like_a_button(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Buttons").click()
        chrome_page.get_by_role("link", name="Looks like a button").click()
        chrome_page.get_by_role("link", name="Click").click()

        expected_result = chrome_page.locator("#result").text_content().strip()
        assert self.ACTUAL_RESULT == expected_result, self.DESCRIPTION_TXT

    def test_disabled(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Buttons").click()
        chrome_page.get_by_role("link", name="Disabled").click()

        select = chrome_page.get_by_role("combobox")
        select.select_option("enabled")
        chrome_page.get_by_role("button", name="Submit").click()

        expected_result = chrome_page.locator("#result").text_content().strip()
        assert self.ACTUAL_RESULT == expected_result, self.DESCRIPTION_TXT
