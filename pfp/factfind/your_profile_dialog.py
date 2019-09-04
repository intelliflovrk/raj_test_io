from selenium.webdriver.common.by import By
from ioffice.base import BasePageSection


class YourProfileDialogue(BasePageSection):
    def __init__(self, parent_page):
        super().__init__(parent_page)

    def click_get_started(self):
        self.page.click(self.Locators.GET_STARTED_BUTTON)
        return self

    class Locators(object):
        GET_STARTED_BUTTON = (By.CSS_SELECTOR, "button[data-dismiss='modal']")
