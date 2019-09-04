from ioffice.leads.base import *


class ViewRelationshipsPage(BaseLeadPage):

    def get_first_relationship_name(self):
        return self.get_text(self.Locators.FIRST_RELATIONSHIP_NAME_LINK)

    def get_first_relationship(self):
        return self.get_text(self.Locators.FIRST_RELATIONSHIP_LINK)

    def get_first_relationship_id(self):
        return self.get_attribute(self.Locators.FIRST_RADIO_BUTTON, "value")

    class Locators(object):
        FIRST_RELATIONSHIP_NAME_LINK = (By.CSS_SELECTOR, "tbody tr td:nth-of-type(2) a")
        FIRST_RELATIONSHIP_LINK = (By.CSS_SELECTOR, "tbody tr td:nth-of-type(3) a")
        FIRST_RADIO_BUTTON = (By.XPATH, "//*[@id='grid_ClientRelationshipsGrid']/tbody/tr/td[1]/input")
