from selenium.webdriver.common.by import By
from ioffice.clients.details.base import BaseDetailsPage


class ClientRelationshipsPage(BaseDetailsPage):

    def get_first_employee_name(self):
        return self.get_text(self.Locators.FIRST_EMPLOYEE_NAME_TEXT)

    def get_first_employee_relationship(self):
        return self.get_text(self.Locators.FIRST_EMPLOYEE_RELATIONSHIP_TEXT)

    def get_relationship_id(self):
        return self.get_attribute(self.Locators.FIRST_RADIO_BUTTON, "value")

    class Locators(object):
        FIRST_EMPLOYEE_NAME_TEXT = (By.XPATH, "//*[@id='grid_ClientRelationshipsGrid']/tbody/tr/td[2]/a")
        FIRST_EMPLOYEE_RELATIONSHIP_TEXT = (By.XPATH, "//*[@id='grid_ClientRelationshipsGrid']/tbody/tr/td[3]/a")
        FIRST_RADIO_BUTTON = (By.XPATH, "//*[@id='grid_ClientRelationshipsGrid']/tbody/tr/td[1]/input")