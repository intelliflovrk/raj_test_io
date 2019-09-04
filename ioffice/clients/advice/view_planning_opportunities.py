from selenium.webdriver.common.by import By
from ioffice.clients.base import BaseClientPage


class ViewPlanningOpportunitiesPage(BaseClientPage):

    def click_first_enter_planning_button(self):
        return self.click(ViewPlanningOpportunitiesPage.Locators.FIRST_ENTER_PLANNING_BUTTON)

    def fill_in_sequential_ref(self, text):
        return self.fill_in_field(ViewPlanningOpportunitiesPage.Locators.SEQUENTIAL_REF_TEXT_BOX, text)

    def click_filter(self):
        return self.click(ViewPlanningOpportunitiesPage.Locators.FILTER_BUTTON)

    class Locators(object):
        FIRST_ENTER_PLANNING_BUTTON = (By.CSS_SELECTOR, '#grid_OpportunitiesGrid tbody tr:not(.filter) a')
        SEQUENTIAL_REF_TEXT_BOX = (By.ID, "id___filterSequentialRef")
        FILTER_BUTTON = (By.CSS_SELECTOR, "#OpportunitiesGrid__ a[onclick*='Filter(this)']")
