import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsSelects:
    EXPECTED = "I am a new page in a new tab"
    DESCRIPTION_TXT = "Cannot refer to a new page"

    def test_new_tab_link(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="New tab").click()
        chrome_page.get_by_role("link", name="New page will be opened on a new tab").click()

        new_page: Page = chrome_page.wait_for_event("popup")
        actual = new_page.locator("#result").inner_text().strip()

        assert self.EXPECTED in actual, self.DESCRIPTION_TXT
        chrome_page.bring_to_front()

    def test_new_tab_button(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="New tab", exact=True).click()
        chrome_page.get_by_role("link", name="New tab button").click()
        chrome_page.get_by_role("link", name="Click").click()

        new_page: Page = chrome_page.wait_for_event("popup")
        actual = new_page.locator("#result").inner_text().strip()

        assert self.EXPECTED in actual, self.DESCRIPTION_TXT
        chrome_page.bring_to_front()
