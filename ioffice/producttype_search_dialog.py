from ioffice.base import BasePageSection, IOFrameDialog
from selenium.webdriver.common.by import By


class ProductTypeSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = ProductTypeSearchDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select(self, product_type_text):
        self.page.select_by_visible_text(ProductTypeSearchDialog.Locators.SELECT_BOX, product_type_text)
        return self

    def click_ok_button(self):
        self.page.click(ProductTypeSearchDialog.Locators.OK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.XPATH,"// iframe[contains(@src,'/nio/PlanType')]")
        SELECT_BOX = (By.ID, "PlanTypeListDropDown")
        OK_BUTTON = (By.XPATH, "//a[text()='OK']")


class GatedProductTypeSearchDialog(BasePageSection, IOFrameDialog):

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = GatedProductTypeSearchDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select(self, product_type_text):
        self.page.select_by_visible_text(GatedProductTypeSearchDialog.Locators.SELECT_BOX, product_type_text)
        return self

    def click_ok_button(self):
        self.page.click(GatedProductTypeSearchDialog.Locators.OK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.XPATH,"// iframe[contains(@src,'/nio/PlanType')]")
        SELECT_BOX = (By.ID, "PlanTypeListDropDown")
        OK_BUTTON = (By.XPATH, "//a[text()='OK']")


class GatedWrapperProductTypeSearchDialog(BasePageSection, IOFrameDialog):
    """A Plan Type Search dialog that opens in Add Sub Plan wizard"""

    def __init__(self, parent_page, current_frame):
        super().__init__(parent_page)
        self.frame_locator = GatedWrapperProductTypeSearchDialog.Locators.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def select(self, product_type_text):
        self.page.select_by_visible_text(GatedProductTypeSearchDialog.Locators.SELECT_BOX, product_type_text)
        return self

    def click_ok_button(self):
        self.page.click(GatedProductTypeSearchDialog.Locators.OK_BUTTON)
        return self

    class Locators(object):
        FRAME = (By.XPATH, "// iframe[contains(@src,'/nio/PlanType')]")
        SELECT_BOX = (By.ID, "PlanTypeListDropDown")
        OK_BUTTON = (By.XPATH, "//a[text()='OK']")


class WrapperProductTypeSearchDialog(BasePageSection, IOFrameDialog):
    pass
