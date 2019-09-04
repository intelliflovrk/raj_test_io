from selenium.webdriver.common.by import By
from ioffice.clients.details.base import BaseDetailsPage


class ViewSummaryPage(BaseDetailsPage):

    def get_address_line_1(self):
        return self.get_text(self.Locators.ADDRESS_LINE_1)

    def get_address_line_2(self):
        return self.get_text(self.Locators.ADDRESS_LINE_2)

    def get_address_line_3(self):
        return self.get_text(self.Locators.ADDRESS_LINE_3)

    def get_address_line_4(self):
        return self.get_text(self.Locators.ADDRESS_LINE_4)

    def get_city_or_town_and_postcode(self):
        return self.get_text(self.Locators.POST_CODE)

    def get_mobile_number(self):
        return self.get_text(self.Locators.MOBILE_NUMBER)

    def get_fax_number(self):
        return self.get_text(self.Locators.FAX_NUMBER)

    def get_service_status(self):
        return self.get_text(self.Locators.SERVICE_STATUS_TEXT)

    def get_fee_model(self):
        return self.get_text(self.Locators.FEE_MODEL)

    def get_campaign_type(self):
        return self.get_text(self.Locators.CAMPAIGN_TYPE)

    def click_second_life(self):
        return self.click(self.Locators.SECOND_LIFE)

    def get_client_relationship_status(self):
        return self.get_text(self.Locators.RELATIONSHIP_STATUS)

    def click_edit(self):
        return self.click(ViewSummaryPage.Locators.EDIT_BUTTON)

    def click_save(self):
        return self.click(ViewSummaryPage.Locators.SAVE_BUTTON)

    def select_service_status(self, status_text):
        return self.select_by_visible_text(ViewSummaryPage.Locators.SERVICE_STATUS_SELECT_BOX, status_text)

    class Locators(object):
        ADDRESS_LINE_1 = (By.ID, "id_AddressLine1_ro")
        ADDRESS_LINE_2 = (By.ID, "id_AddressLine2_ro")
        ADDRESS_LINE_3 = (By.ID, "id_AddressLine3_ro")
        ADDRESS_LINE_4 = (By.ID, "id_AddressLine4_ro")
        POST_CODE = (By.CSS_SELECTOR, "#id_CityTownPostCode_ro")
        MOBILE_NUMBER = (By.CSS_SELECTOR, "#id_MobileNum_ro")
        SERVICE_STATUS_TEXT = (By.CSS_SELECTOR, "[for='ServiceStatusId'] + span")
        FAX_NUMBER = (By.CSS_SELECTOR, "#id_Fax_ro")
        FEE_MODEL = (By.CSS_SELECTOR, "#FeeModelContainer > div > span")
        SECOND_LIFE = (By.CSS_SELECTOR, "#id_RelatedPartyName")
        CAMPAIGN_TYPE = (By.CSS_SELECTOR, "#id_CampaignTypeId")
        RELATIONSHIP_STATUS = (By.CSS_SELECTOR, "[for='id_RelatedPartyName']")
        EDIT_BUTTON = (By.ID, "SummaryForm_9")
        SAVE_BUTTON = (By.ID, "SummaryForm_8")
        SERVICE_STATUS_SELECT_BOX = (By.ID, "ServiceStatusId")
