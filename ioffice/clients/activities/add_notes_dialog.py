from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection, IOFrameDialog


class AddNotesDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.frame_locator = AddNotesDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def fill_in_note_details(self, note_text):
        self.page.fill_in_field(AddNotesDialog.Locators.NOTES_DETAILS_TEXT_BOX, note_text)
        return self

    def click_save(self):
        self.page.click(AddNotesDialog.Locators.SAVE_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.CSS_SELECTOR, "iframe[src*='OpenAddTaskNotes']")
        NOTES_DETAILS_TEXT_BOX = (By.ID, "id_Notes")
        SAVE_BUTTON = (By.XPATH, "//a[text()='Save']")
