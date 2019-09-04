from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from ioffice.clients.activities.base import ActivitiesBasePage
from selenium.webdriver.common.by import By


class TasksAndApptsPage(ActivitiesBasePage):

    def get_activity_table_rows(self):
        return WebDriverWait(self.driver, self.TIMEOUT)\
            .until(EC.presence_of_all_elements_located(TasksAndApptsPage.Locators.CLIENT_ACTIVITY_ROW))

    def check_select_all_activities(self):
        return self.click(TasksAndApptsPage.Locators.SELECT_ALL_ACTIVITIES_CHECKBOX)

    def click_delete(self):
        return self.click(TasksAndApptsPage.Locators.DELETE_BUTTON)

    def fill_in_assigned_to_text_box(self, data):
        self.clear_and_fill_in_field(self.Locators.ASSINGNED_TO_TEXT_BOX, data)
        return self

    def click_filter_button(self):
        self.click(self.Locators.FILTER_BUTTON)
        return self

    def click_first_open_link(self):
        return self.click(TasksAndApptsPage.Locators.OPEN_LINKS)

    def click_pick_task_fliter(self):
        return self.click(TasksAndApptsPage.Locators.PICK_TASK_FILTER_BUTTON)

    def click_all_tasks_and_appts(self):
        return self.click(TasksAndApptsPage.Locators.ALL_TASKS_AND_APPTS_FILTER_LINK)

    class Locators(object):
        CLIENT_ACTIVITY_ROW = (By.CSS_SELECTOR, "#grid_ClientTaskOpenActivityGrid tbody tr:not(.filter)")
        SELECT_ALL_ACTIVITIES_CHECKBOX = (By.CSS_SELECTOR, "#grid_ClientTaskOpenActivityGrid thead [type='checkbox']")
        FILTER_BUTTON = (By.XPATH, "//*[@id='ClientTaskOpenActivityGrid__']/td[14]/a[1]")
        ASSINGNED_TO_TEXT_BOX = (By.ID, "id___filterAssignedToUserName")
        DELETE_BUTTON = (By.CSS_SELECTOR, "#ClientTaskOpenActivityGrid_17")
        OPEN_LINKS = (By.CSS_SELECTOR, "tbody a[href*='ViewClientActivity']")
        PICK_TASK_FILTER_BUTTON = (By.CSS_SELECTOR, '.dropPickerHandle a')
        ALL_TASKS_AND_APPTS_FILTER_LINK = (By.CSS_SELECTOR, ".dropPickerItem a[href='?filter2=all']")
