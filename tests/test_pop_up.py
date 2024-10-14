import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsPopUps:
    DESCRIPTION_TXT = "Cannot to interact with pop-up"

    @pytest.mark.parametrize("select, expected", [(True, "select me or not"), (False, "None")])
    def test_modal(self, chrome_page: Page, select: bool, expected: str):
        chrome_page.get_by_role("link", name="Pop-Up", exact=True).click()
        chrome_page.get_by_role("button", name="Launch Pop-Up").click()
        if select:
            chrome_page.get_by_role("checkbox", name=expected.capitalize()).click()
        chrome_page.get_by_role("button", name="Send").click()

        actual = chrome_page.locator("#result").inner_text().strip()
        assert expected in actual, self.DESCRIPTION_TXT

    @pytest.mark.parametrize("select, expected", [(True, "Correct"), (False, "Nope")])
    def test_iframe_pop_up(self, chrome_page: Page, select: bool, expected: str):
        text_to_copy = "Something"
        chrome_page.get_by_role("link", name="Pop-Up", exact=True).click()
        chrome_page.get_by_role("link", name="Iframe Pop-Up").click()
        chrome_page.get_by_role("button", name="Launch Pop-Up").click()

        if select:
            text_to_copy = chrome_page.locator("iframe").content_frame.get_by_text("I am the text you want to copy").inner_text()

        chrome_page.get_by_role("button", name="Check").click()
        chrome_page.get_by_placeholder("Put the text you copied in").fill(text_to_copy)
        chrome_page.get_by_role("button", name="Submit").click()

        actual = chrome_page.wait_for_selector("#check-result").inner_text()
        assert expected in actual, self.DESCRIPTION_TXT
