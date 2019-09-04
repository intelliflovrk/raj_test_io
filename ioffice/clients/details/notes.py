from ioffice.clients.details.base import BaseDetailsPage
from selenium.webdriver.common.by import By


class Notes(BaseDetailsPage):
    def get_notes(self):
        return self.get_text(self.Locators.NOTES)

    class Locators(object):
        NOTES = (By.CSS_SELECTOR, ".client-note-content")

