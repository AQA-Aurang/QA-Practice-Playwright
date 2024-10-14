import pytest
from playwright.sync_api import Page


@pytest.mark.usefixtures("chrome_page")
class TestsDragAndDrops:
    EXPECTED = "Dropped"
    DESCRIPTION_TXT = "Cannot drag or drag and drop element"

    def test_boxes(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Drag and Drop").click()
        draggable_element = chrome_page.locator("#rect-draggable")
        droppable_area = chrome_page.locator("#rect-droppable")
        draggable_element.drag_to(target=droppable_area)

        actual = chrome_page.wait_for_selector("#rect-droppable").inner_text()
        assert self.EXPECTED in actual, self.DESCRIPTION_TXT

    def test_images(self, chrome_page: Page):
        chrome_page.get_by_role("link", name="Drag and Drop").click()
        chrome_page.get_by_role("link", name="Images").click()
        draggable_element = chrome_page.locator("//div[@id='rect-droppable1']//img[1]")
        droppable_area = chrome_page.locator("#rect-droppable2")
        draggable_element.drag_to(target=droppable_area)

        actual = chrome_page.wait_for_selector("#rect-droppable2").inner_text()
        assert self.EXPECTED in actual, self.DESCRIPTION_TXT
