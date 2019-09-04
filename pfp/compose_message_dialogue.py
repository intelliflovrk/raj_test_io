from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection


class ComposeMessageDialogue(BasePageSection):
    def __init__(self, parent_page):
        super().__init__(parent_page)

    def fill_in_subject(self, text):
        self.page.fill_in_field(self.Locators.SUBJECT_FIELD, text)
        return self

    def fill_in_body(self, text):
        self.page.fill_in_field(self.Locators.MESSAGE_TEXT_BOX, text)
        return self

    def click_send(self):
        self.page.click(self.Locators.SEND_BUTTON)
        return self

    class Locators(object):
        SUBJECT_FIELD = (By.ID, 'compose-subject')
        MESSAGE_TEXT_BOX = (By.ID, 'compose-message')
        SEND_BUTTON = (By.ID, 'send-message-btn')
