from selenium.webdriver.common.by import By
from ioffice.plans.base_summary import BasePlanSummaryPage


class WrapPlanSummaryPage(BasePlanSummaryPage):

    def fill_in_report_notes(self, text):
        return self.fill_in_field(WrapPlanSummaryPage.Locators.REPORT_NOTES_TEXT_BOX, text)

    def click_save(self):
        return self.click(WrapPlanSummaryPage.Locators.SAVE_BUTTON)

    class Locators(object):
        REPORT_NOTES_TEXT_BOX = (By.ID, "id_PolicyBusiness_PolicyBusinessExt_ReportNotes")
        SAVE_BUTTON = (By.ID, "DefaultSummaryContainer_4_13")
