from ioffice.base import *


class BaseLeadPage(IOBasePage):

    def get_lead_bar_info(self):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(BaseLeadPage.Locators.BAR_INFO)).text

    def lead_actions_menu(self):
        return LeadActionsMenuSection(self)

    def click_add_lead(self):
        return self.click(BaseLeadPage.Locators.ADD_LEAD)

    def click_activities(self):
        return self.click(BaseLeadPage.Locators.ACTIVITIES_TAB)

    def click_details(self):
        return self.click(BaseLeadPage.Locators.DETAILS_TAB)

    class Locators(object):
        BAR_INFO = (By.XPATH, "//div[@class='bar-info']/strong")
        ADD_LEAD = (By.XPATH, "/html/body/div[5]/ul/li/a")
        ACTIONS_MENU = (By.ID, "primary")
        ACTIVITIES_TAB = (By.CSS_SELECTOR, ".menu_node_lead_Tasks")
        DETAILS_TAB = (By.CSS_SELECTOR, ".menu_node_lead_detail")


class LeadActionsMenuSection(BasePageSection, BasePage):

    def hover_over_lead_actions(self):
        return self.hover_over(BaseLeadPage.Locators.ACTIONS_MENU)

    def change_status(self):
        return self.click(LeadActionsMenuSection.Locators.CHANGE_STATUS_LINK)

    def click_add_task(self):
        return self.click(LeadActionsMenuSection.Locators.ADD_TASK_LINK)

    def click_upload_document(self):
        return self.click(LeadActionsMenuSection.Locators.UPLOAD_DOCUMENT_LINK)

    def click_add_relationship(self):
        return self.click(LeadActionsMenuSection.Locators.ADD_RELATIONSHIP_LINK)

    class Locators(object):
        CHANGE_STATUS_LINK = (By.XPATH, "//*[contains(text(),'Change Status')]")
        ADD_TASK_LINK = (By.XPATH, "//*[contains(text(),'Add Task')]")
        UPLOAD_DOCUMENT_LINK = (By.XPATH, "//*[contains(text(),'Upload Document')]")
        ADD_RELATIONSHIP_LINK = (By.XPATH, "//*[contains(text(),'Add Relationship')]")