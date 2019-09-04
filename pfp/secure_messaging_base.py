from pfp.base import PFPBasePage
from selenium.webdriver.common.by import By


class BaseSecureMessagingPage(PFPBasePage):

    def click_sent_messages(self):
        return self.click(self.Locators.SENT_MESSAGES_TAB)

    class Locators(object):
        SENT_MESSAGES_TAB = (By.ID, 'message-sent')