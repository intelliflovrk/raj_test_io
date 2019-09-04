from selenium.webdriver.common.by import By
from ioffice.organiser.base import BaseOrganiserPage
from pageobjects import BasePageSection, BasePage


class TasksPage(BaseOrganiserPage):
    def is_title_matches(self):
        return "User Tasks | Intelligent Office" == self.driver.title

    def level3_menu(self):
        return IoLevel3NavigationMenuSection(self)

    def check_select_all_tasks(self):
        return self.click(TasksPage.Locators.SELECT_ALL_TASKS_CHECKBOX)

    def click_delete(self):
        return self.click(TasksPage.Locators.DELETE_BUTTON)

    def click_date_filter(self):
        return self.click(TasksPage.Locators.DATE_FILTER)

    def click_all_open_date(self):
        return self.click(TasksPage.Locators.ALL_OPEN_DATE)

    def get_start_date_cell_value(self):
        return self.get_text(TasksPage.Locators.TASKS_FIRST_COLUMN_CELL)

    def get_due_date_cell_value(self):
        return self.get_text(TasksPage.Locators.TASKS_SECOND_COLUMN_CELL)

    def get_subject_cell_value(self):
        return self.get_text(TasksPage.Locators.TASKS_FIFTH_COLUMN_CELL)

    def get_activity_type_cell_value(self):
        return self.get_text(TasksPage.Locators.TASKS_FORTH_COLUMN_CELL)

    class Locators(object):
        CLIENT_ACTIVITY_ROW = (By.CSS_SELECTOR, "#grid_ClientTaskOpenActivityGrid tbody tr:not(.filter)")
        DATE_FILTER = (By.CSS_SELECTOR, "#id_root_2_2_3 > div > div:nth-child(2) > div")
        ALL_OPEN_DATE = (By.CSS_SELECTOR,
                         "#id_root_2_2_3 > div > div:nth-child(2) > div > div.dropPickerBody > div:nth-child(2) > a")
        SELECT_ALL_ACTIVITIES_CHECKBOX = (By.CSS_SELECTOR, "#grid_ClientTaskOpenActivityGrid thead [type='checkbox']")
        TASKS_FIRST_COLUMN_CELL = (By.XPATH, "//*[@id='grid_CRMTaskGrid']/tbody/tr[2]/td[2]/span")
        TASKS_SECOND_COLUMN_CELL = (By.XPATH, "//*[@id='grid_CRMTaskGrid']/tbody/tr[2]/td[3]/span")
        TASKS_FORTH_COLUMN_CELL = (By.XPATH, "//*[@id='grid_CRMTaskGrid']/tbody/tr[2]/td[5]/span")
        TASKS_FIFTH_COLUMN_CELL = (By.XPATH, "//*[@id='grid_CRMTaskGrid']/tbody/tr[2]/td[6]/span")
        SELECT_ALL_TASKS_CHECKBOX = (By.CSS_SELECTOR, "#grid_CRMTaskGrid thead [type='checkbox']")
        DELETE_BUTTON = (By.CSS_SELECTOR, "#CRMTaskGrid_20")


class IoLevel3NavigationMenuSection(BasePageSection, BasePage):

    def click_my_tasks(self):
        return self.click(IoLevel3NavigationMenuSection.Locators.MY_TASKS_TAB)

    class Locators(object):
        MY_TASKS_TAB = (By.CSS_SELECTOR, "ul.nav-tertiary.group > li:nth-child(1) > a")
