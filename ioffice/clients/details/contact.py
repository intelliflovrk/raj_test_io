from ioffice.clients.details.base import BaseDetailsPage
from selenium.webdriver.common.by import By


class Contact(BaseDetailsPage):

    def get_contact(self):
        return self.get_text(Contact.Locators.VALUE_FIELD)

    class Locators(object):
        VALUE_FIELD = (By.CSS_SELECTOR, "td:nth-child(3)")
