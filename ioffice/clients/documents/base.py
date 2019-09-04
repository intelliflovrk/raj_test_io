from ioffice.clients.base import *


class BaseDocumentsPage(BaseClientPage):

    def click_document_queue(self):
        self.click(BaseDocumentsPage.Locators.DOCUMENT_QUEUE_TAB)
        return self

    def click_binders(self):
        return self.click(BaseDocumentsPage.Locators.BINDERS_TAB)

    class Locators(object):
        DOCUMENT_QUEUE_TAB = (By.XPATH, "//*[@id='sidebar-container']//div[text()='Document Queue']")
        BINDERS_TAB = (By.CSS_SELECTOR, ".tabTabs a[href*='Binder']")
