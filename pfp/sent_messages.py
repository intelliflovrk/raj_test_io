from pfp.secure_messaging_base import BaseSecureMessagingPage
from selenium.webdriver.common.by import By


class SentMessagesPage(BaseSecureMessagingPage):

    def get_message_title(self):
        return self.get_text(self.Locators.FIRST_ROW_TITLE_TEXT)

    class Locators(object):
        FIRST_ROW_TITLE_TEXT = (By.CSS_SELECTOR, '#messages-sent-table-body > a:nth-child(1) .message-title')