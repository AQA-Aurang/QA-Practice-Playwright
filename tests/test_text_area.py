import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsTextAreas:
    TEXT_FOR_FILL = "Some text in text area"
    DESCRIPTION_TXT = "Cannot to interact with text area"

    def test_textarea(self, chrome_page: Page):
        chrome_page.locator("#sidebar").get_by_role("link", name="Text area").click()
        textarea = chrome_page.get_by_role("textbox", name="Text area")
        textarea.fill(self.TEXT_FOR_FILL)
        chrome_page.get_by_role("button", name="Submit").click()

        expected_result = chrome_page.locator("#result").inner_text().strip()
        assert self.TEXT_FOR_FILL in expected_result, self.DESCRIPTION_TXT

    @pytest.mark.parametrize("chapters", [["second"], ["third"], ["second", "third"]])
    def test_multiple_textarea(self, chrome_page: Page, chapters: str):
        chrome_page.locator("#sidebar").get_by_role("link", name="Text area").click()
        chrome_page.get_by_role("link", name="Multiple textareas").click()

        chrome_page.locator("#id_first_chapter").fill("Some text in 1st textarea")

        inputted_texts: list[str] = []
        for chapter in chapters:
            another_textarea = chrome_page.locator(f"#id_{chapter}_chapter")
            text_in_another_chapter = f"Hey its text in the {chapter} chapter"
            inputted_texts.append(text_in_another_chapter)
            another_textarea.fill(text_in_another_chapter)

        chrome_page.get_by_role("button", name="Submit").click()

        expected_result = chrome_page.locator("#result").inner_text().strip()
        assert "Some text in 1st textarea" in expected_result, "Cannot to interact with 1st textarea"

        if len(inputted_texts) == 1:
            assert inputted_texts[0] in expected_result, "Cannot get text from another chapter"
            return

        assert inputted_texts[0] in expected_result, "Cannot get text from 2nd chapter"
        assert inputted_texts[1] in expected_result, "Cannot get text from 3rd chapter"
