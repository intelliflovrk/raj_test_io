from ioffice.wizard import *
from ioffice.select_delegate_dialog import *


class DelegateInDialog(BasePageSection, IOFrameDialog, BasePage):
    def __init__(self, parent_page, current_frame=None):
        super().__init__(parent_page)
        self.FRAME = (By.XPATH, DelegateInDialog.Locators._FRAME)
        self.frame_locator = self.FRAME
        self.prev_frame_locator = current_frame
        self._switch_to_frame()

    def open_delegate_search_dialog(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(DelegateInDialog.Locators.SEARCH)).click()
        return SelectDelegateDialog(self, self.frame_locator, "id_DelegatePartyId")

    def click_delegate_in_button(self):
        return self.page.click(DelegateInDialog.Locators.DELEGATE_IN_BUTTON)

    class Locators(object):
        _FRAME = "//iframe[@src='/nio/system/userpanel?a=delegate']"
        DELEGATE_IN_BUTTON = (By.ID, "DelegateAutocomplete_3")
        SEARCH = (By.CSS_SELECTOR, "#DelegateAutocomplete_2 > div.formgroupbody > div > div > span > div > a.hpick")
