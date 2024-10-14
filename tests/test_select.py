import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsSelects:
    DESCRIPTION_TXT = "Cannot select any variant"

    def test_single_select(self, chrome_page: Page):
        language = "Python"

        chrome_page.get_by_role("link", name="Select", exact=True).click()
        select = chrome_page.get_by_role("combobox")
        select.select_option(label=language)
        chrome_page.get_by_role("button", name="Submit").click()

        expected_result = chrome_page.locator("#result").inner_text().strip()
        assert language in expected_result, self.DESCRIPTION_TXT

    def test_multiple_select(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Select", exact=True).click()
        chrome_page.get_by_role("link", name="Multiple selects").click()

        select_place = chrome_page.locator("#id_choose_the_place_you_want_to_go")
        select_place.select_option(label="Sea")

        select_vehicle = chrome_page.locator("#id_choose_how_you_want_to_get_there")
        select_vehicle.select_option(label="Air")

        select_time = chrome_page.locator("#id_choose_when_you_want_to_go")
        select_time.select_option(label="Today")

        chrome_page.get_by_role("button", name="Submit").click()

        expected_result = chrome_page.locator("#result").inner_text().strip()
        assert "Sea".lower() in expected_result, self.DESCRIPTION_TXT
        assert "Air".lower() in expected_result, self.DESCRIPTION_TXT
        assert "Today".lower() in expected_result, self.DESCRIPTION_TXT
