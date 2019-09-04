from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.alert import Alert


class BasePage(object):
    """Base class to initialize the base page that will be called from all pages"""
    TIMEOUT = 60

    def __init__(self, config):
        self.driver = config.driver
        self.config = config

    def switch_tab(config, num):
        config.driver.switch_to.window(config.driver.window_handles[num])

    def fill_in_field(self, locator, data):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator)).send_keys(data)
        return self

    def clear_and_fill_in_field(self, locator, data):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator)).clear()
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator)).send_keys(data)
        return self

    def fill_in_form(self, data, page):
        for b in data:
            if b.isupper():
                self.fill_in_field(page.Locators.__dict__.get(b), data[b])
        return self

    def clear(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator)).clear()
        return self

    def get_text(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator)).text

    def get_attribute(self, locator, attribute):
        return WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator)).get_attribute(attribute)

    def get_drop_down_selected_value(self, locator):
        select_object = Select(
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator)))
        menu_value = select_object.first_selected_option.text
        return menu_value

    def click(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator)).click()
        return self

    def key_enter(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator)).send_keys(Keys.RETURN)
        return self

    def hover_over(self, locator):
        element_to_hover_over = WebDriverWait(self.driver, self.TIMEOUT).until(
            EC.presence_of_element_located(locator))
        ActionChains(self.driver).move_to_element(element_to_hover_over).perform()
        return self

    def select_by_visible_text(self, locator, text):
        el = WebDriverWait(self.driver, BasePage.TIMEOUT).until(
            EC.presence_of_element_located(locator))
        Select(el).select_by_visible_text(text)
        return self

    def select_by_index(self, locator, index):
        el = WebDriverWait(self.driver, BasePage.TIMEOUT).until(
            EC.presence_of_element_located(locator))
        Select(el).select_by_index(index)
        return self

    def select_by_value(self, locator, value):
        el = WebDriverWait(self.driver, BasePage.TIMEOUT).until(
            EC.presence_of_element_located(locator))
        Select(el).select_by_value(value)
        return self

    def click_ok_in_browser_confirmation_dialog(self):
        return Alert(self.driver).accept()

    def is_radio_button_selected(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(locator)).is_selected()

    def select_text_and_delete(self, locator):
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator)).send_keys(
            Keys.CONTROL + 'a')
        WebDriverWait(self.driver, self.TIMEOUT).until(EC.element_to_be_clickable(locator)).send_keys(Keys.DELETE)
        return self

    def get_table_rows(self, locator):
        return WebDriverWait(self.driver, self.TIMEOUT).until(EC.presence_of_all_elements_located(locator))


class FrameDialog(object):

    TIMEOUT = 60

    def __init__(self, frame_locator=None, prev_frame_locator=None, popup_control=None):
        self.frame_locator = frame_locator
        self.prev_frame_locator = prev_frame_locator
        self.popup_control = popup_control

    def _switch_to_frame(self):
        self.driver.switch_to.default_content()
        if self.frame_locator:
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.frame_to_be_available_and_switch_to_it(self.frame_locator))
        else:
            raise Exception("frame_locator is not set for the frame page, set this in your page __init__")
        return self

    def _switch_to_previous_frame(self):
        self.driver.switch_to.default_content()
        WebDriverWait(self.driver, self.TIMEOUT).until_not(EC.presence_of_element_located(self.frame_locator))
        if self.prev_frame_locator:
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.visibility_of_element_located(self.prev_frame_locator))
            WebDriverWait(self.driver, self.TIMEOUT).until(EC.frame_to_be_available_and_switch_to_it(self.prev_frame_locator))

    def close_dialog(self):
        self._switch_to_previous_frame()
        return self


class BasePageSection(object):

    def __init__(self, parent_page):
        self.page = parent_page
        self.driver = parent_page.driver
        self.config = parent_page.config