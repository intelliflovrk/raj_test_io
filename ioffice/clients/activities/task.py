from ioffice.clients.activities.base import BasePageSection
from selenium.webdriver.common.by import By

from ioffice.clients.base import BaseClientPage


class ClientTaskBasePage(BaseClientPage):

    def task_navigation_menu(self):
        return TaskNavigationMenuSection(self)


class TaskNavigationMenuSection(BasePageSection):

    def click_details(self):
        self.page.click(self.Locators.DETAILS_TAB)
        return TaskDetailsPage(self.config)

    def click_documents(self):
        self.page.click(self.Locators.DOCUMENTS_TAB)
        return TaskDocumentsPage(self.config)

    class Locators(object):
        DETAILS_TAB = (By.XPATH, "//div[@class='ux-lib-tbody' and text()='Details']")
        DOCUMENTS_TAB = (By.XPATH, "//div[@class='ux-lib-tbody' and text()='Documents']")


class TaskDetailsPage(ClientTaskBasePage):
    def __init__(self, config):
        super().__init__(config)

    def hover_over_task_actions(self):
        self.hover_over(TaskDetailsPage.Locators.TASK_ACTIONS_MENU)
        return TaskActionsMenuSection(self)

    def get_mobile(self):
        return self.get_text(TaskDetailsPage.Locators.MOBILE_TEXT)

    def get_address(self):
        return self.get_text(TaskDetailsPage.Locators.ADDRESS_TEXT)

    def get_assigned_to(self):
        return self.get_text(TaskDetailsPage.Locators.ASSIGNED_TO_TEXT)

    def get_status(self):
        return self.get_drop_down_selected_value(TaskDetailsPage.Locators.STATUS_SELECT_BOX)

    def get_note(self):
        return self.get_text(TaskDetailsPage.Locators.NOTE_TEXT)

    class Locators(object):
        TASK_ACTIONS_MENU = (By.ID, 'secondary')
        ADDRESS_TEXT = (By.ID, "id_ClientAddress_ro")
        MOBILE_TEXT = (By.ID, "id_ClientMobile_ro")
        ASSIGNED_TO_TEXT = (By.ID, "id_AssignedToName_ro")
        STATUS_SELECT_BOX = (By.ID, "StatusDropDown")
        NOTE_TEXT = (By.CSS_SELECTOR, ".task-note-content")


class TaskDocumentsPage(ClientTaskBasePage):
    def __init__(self, config):
        super().__init__(config)

    def get_last_updated_date(self):
        return self.get_text(self.Locators.LAST_UPDATED_TEXT)

    class Locators(object):
        LAST_UPDATED_TEXT = (By.XPATH, '//*[@id="id_root_2_2_7_5_2_2_2"]//table/tbody/tr/td[6]')


class TaskActionsMenuSection(BasePageSection):
    def click_add_a_task_note(self):
        self.page.click(TaskActionsMenuSection.Locators.ADD_A_TASK_NOTE_LINK)
        return self

    def click_upload_document(self):
        self.page.click(TaskActionsMenuSection.Locators.UPLOAD_DOCUMENT_LINK)
        return self

    class Locators(object):
        ADD_A_TASK_NOTE_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Add Notes']")
        UPLOAD_DOCUMENT_LINK = (By.CSS_SELECTOR, "#secondary a[onclick*= 'Upload Document']")
