from selenium.webdriver.common.by import By
from ioffice.clients.factfind.base import BaseFactFindPage


class SummaryStage(BaseFactFindPage):

    def fill_in_consent_date_fields(self, data):
        return self.fill_in_field(SummaryStage.Locators.CONSENT_DATE, data)

    def click_marketing_subtab(self):
        return self.click(SummaryStage.Locators.MARKETING_SUBTAB)

    class Locators(BaseFactFindPage):
        MARKETING_SUBTAB = (By.LINK_TEXT, "Marketing")
        CONSENT_DATE = (By.ID, "ConsentDate_ConsentDate_0")
