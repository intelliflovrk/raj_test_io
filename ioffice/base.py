import time
from pageobjects import BasePage, BasePageSection, FrameDialog
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class IOBasePage(BasePage):
    """Base page for all IO authenticated pages"""

    def level1_menu(self):
        return IoLevel1NavigationMenuSection(self)

    def level2_menu(self):
        return IoLevel2NavigationMenuSection(self)

    def click_go_button(self):
        return self.click(IOBasePage.Locators.GO_BUTTON)

    def fill_in_client_search_field(self, data):
        return self.fill_in_field(IOBasePage.Locators.CLIENT_SEARCH, data)

    def selected_area_is_not(self, area):
        return self.get_text(IoLevel1NavigationMenuSection.Locators.SELECTED_AREA) != area

    def get_selected_area_text(self):
        return self.get_text(IoLevel1NavigationMenuSection.Locators.USER_NAVIGATION_MENU)

    def get_logged_in_username(self):
        return self.get_text(IoLevel1NavigationMenuSection.Locators.USER_NAVIGATION_MENU).split()[-1]

    def wait_until_please_wait_spinner_present(self):
        WebDriverWait(self.driver, self.TIMEOUT).until_not(
            EC.presence_of_element_located(IOBasePage.Locators.BLOCK_UI))
        return self

    class Locators(object):
        GO_BUTTON = (By.XPATH, "//*[@value='Go']")
        CLIENT_SEARCH = (By.ID, "client_search")
        BLOCK_UI = (By.XPATH, "//div[@class='blockUI blockOverlay']")


class IOFrameDialog(FrameDialog):

    def close_io_dialog(self):
        self.close_dialog()
        self.wait_until_please_wait_spinner_present()
        return self

    def wait_until_please_wait_spinner_present(self):
        WebDriverWait(self.driver, self.TIMEOUT) \
            .until_not(EC.presence_of_element_located(IOFrameDialog.Locators.BLOCK_UI))
        return self

    class Locators(object):
        BLOCK_UI = (By.XPATH, "//div[@class='blockUI blockOverlay']")


class IoLevel1NavigationMenuSection(BasePageSection):

    def hover_over_navigation_menu(self):
        time.sleep(5)
        self.page.hover_over(IoLevel1NavigationMenuSection.Locators.NAVIGATION_MENU)
        return self

    def click_administration(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.ADMINISTRATION_LINK)
        return self

    def click_mi_reports(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.MI_REPORTS_LINK)
        return self

    def click_compliance(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.COMPLIANCE)
        return

    def click_organiser(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.ORGANISER)
        return

    def click_adviserworkplace(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.ADVISERWORKPLACE_LINK)
        return self

    def click_iostore(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.IOSTORE_LINK)
        return self

    def click_income(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.INCOME)
        return self

    def click_home(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.HOME_LINK)
        return self

    def hover_over_user_navigation_menu(self):
        self.page.hover_over(IoLevel1NavigationMenuSection.Locators.USER_NAVIGATION_MENU)
        return self

    def click_logout(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.LOGOUT_LINK)
        return self

    def click_delegate_in(self):
        self.page.click(IoLevel1NavigationMenuSection.Locators.DELEGATE_IN_LINK)
        return self

    class Locators(object):
        """A class for top level navigation locators"""
        LOGOUT_LINK = (By.XPATH, '//ul[@id="nav-user-drop"]/li/a[contains(@href, "logoff")]')
        DELEGATE_IN_LINK = (By.XPATH, '//*[@id="nav-user-drop"]/li/a[contains(text(), "Delegate In")]')
        ADMINISTRATION_LINK = (By.CSS_SELECTOR, '[href="/nio/user/index"]')
        ADVISERWORKPLACE_LINK = (By.XPATH, '//*[@id="nav-app"]//*[@href="/nio/clientsearch/index"]')
        INCOME_LINK = (By.CSS_SELECTOR, '[href="/nio/providerstatement/index"]')
        IOSTORE_LINK = (By.XPATH, '//ul[@id="nav-app-drop"]/li/a[contains(@href, "/nio/iostore/index")]')
        NAVIGATION_MENU = (By.ID, "nav-app")
        USER_NAVIGATION_MENU = (By.ID, "nav-user")
        HOME_LINK = (By.CLASS_NAME, "io-icon-home")
        SELECTED_AREA = (By.CSS_SELECTOR, '#nav-app > a')
        MI_REPORTS_LINK = (By.CSS_SELECTOR, "[href='\/nio\/mireports\/index']")
        INCOME = (By.CSS_SELECTOR, "[href='\/nio\/providerstatement\/index']")
        COMPLIANCE = (By.CSS_SELECTOR, "[href='/nio/presalefilecheck/viewpresalesearch']")
        ORGANISER = (By.CSS_SELECTOR, "[href='/nio/organiser/listusertasks']")
        HEAD_WRAPPER = (By.CSS_SELECTOR, ".dashboard-page")


class IoLevel2NavigationMenuSection(BasePageSection):

    def click_uploads(self):
        self.page.click(self.Locators.UPLOADS)
        return self

    def click_dashboard(self):
        self.page.click(self.Locators.UPLOADS)
        return self

    def click_file_checking(self):
        self.page.click(self.Locators.FILE_CHECKING)
        return self

    class Locators(object):
        UPLOADS = (By.CSS_SELECTOR, '.menu_node_home_uploads')
        FILE_CHECKING = (By.CSS_SELECTOR, '.menu_node_compliance_filecheck')


