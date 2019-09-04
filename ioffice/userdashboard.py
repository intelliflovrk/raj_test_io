from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from ioffice.base import IOBasePage
from pageobjects import BasePageSection, BasePage


class UserDashboardPage(IOBasePage):

    def is_title_matches(self):
        return "Home | Dashboard | My Dashboard | Intelligent Office" == self.driver.title

    def level3_menu(self):
        return IoLevel3NavigationMenuSection(self)

    def click_my_tasks(self):
        return self.click(UserDashboardPage.Locators.MY_TASKS)

    def click_individual_task_in_widget(self):
        return self.click(UserDashboardPage.Locators.INDIVIDUAL_TASK)

    def click_add_client(self):
        return self.click(UserDashboardPage.Locators.ADD_CLIENT)

    def click_add_client_and_plan(self):
        return self.click(UserDashboardPage.Locators.ADD_CLIENT_AND_PLAN)

    def click_quick_add_client(self):
        return self.click(UserDashboardPage.Locators.QUICK_ADD_CLIENT_LINK)

    def get_recent_clients(self):
        return WebDriverWait(self.driver, 30).until(
            EC.presence_of_element_located(UserDashboardPage.Locators.MY_RECENT_CLIENTS)).text

    class Locators(object):
        ADD_CLIENT_AND_PLAN = (By.XPATH, "//div[@class='quicklinks-wrapper group']//a[contains(text(), 'Add Client And Plan')]")
        ADD_CLIENT = (By.XPATH, "//div[@class='quicklinks-wrapper group']//a[contains(text(), 'Add Client')]")
        MY_RECENT_CLIENTS = (By.CSS_SELECTOR, ".content-list")
        QUICK_ADD_CLIENT_LINK = (By.XPATH, "//ul[@class='nav-quicklinks']//a[text()='Quick Add Client']")
        MY_TASKS = (By.XPATH, "//a[.='My Tasks']")
        INDIVIDUAL_TASK = (By.CSS_SELECTOR, "[onclick *= 'viewactivitydialogbytaskid']")


class IoLevel3NavigationMenuSection(BasePageSection, BasePage):

    def click_my_dashboard(self):
        self.page.click(self.Locators.MY_DASHBOARD)
        return self

    class Locators(object):
        MY_DASHBOARD = (By.CSS_SELECTOR, '.menu_node_home_user_dashboard')
