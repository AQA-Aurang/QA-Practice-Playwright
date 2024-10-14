import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsCheckboxes:
    CHECKBOX_TITLE = "select me or not"
    DESCRIPTION_TXT = "Cannot push action with checkbox"

    def test_single_checkbox(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Checkbox", exact=True).click()
        checkbox = chrome_page.get_by_role("checkbox", name=self.CHECKBOX_TITLE.capitalize())

        if not checkbox.is_checked():
            checkbox.check()
            chrome_page.keyboard.press("Enter")

            expected_result = chrome_page.locator("#result").inner_text().strip()
            assert self.CHECKBOX_TITLE in expected_result, self.DESCRIPTION_TXT

    @pytest.mark.parametrize("checkbox_item", ["One", "Two", "Three"])
    def test_checkboxes(self, chrome_page: Page, checkbox_item: str):
        chrome_page.get_by_role("link", name="Checkbox", exact=True).click()
        chrome_page.get_by_role("link", name="Checkboxes").click()
        checkbox = chrome_page.get_by_role("checkbox", name=checkbox_item)

        if not checkbox.is_checked():
            checkbox.check()
            chrome_page.keyboard.press("Enter")

            expected_result = chrome_page.locator("#result").inner_text().strip()
            assert checkbox_item.lower() in expected_result, self.DESCRIPTION_TXT

    def test_all_checkboxes(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Checkbox", exact=True).click()
        chrome_page.get_by_role("link", name="Checkboxes").click()

        list_of_title_selected_item = []
        for i in range(3):
            checkbox = chrome_page.locator(f"#id_checkboxes_{i}")
            label = chrome_page.locator(f"//label[@for='id_checkboxes_{i}']")
            list_of_title_selected_item.append(label.inner_text())

            if not checkbox.is_checked():
                checkbox.check()

        chrome_page.keyboard.press("Enter")
        titles_in_str = ", ".join(list_of_title_selected_item)

        expected_result = chrome_page.locator("#result").text_content().strip()
        assert titles_in_str.lower() in expected_result, self.DESCRIPTION_TXT
