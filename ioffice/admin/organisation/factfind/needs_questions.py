from ioffice.base import BasePage
from selenium.webdriver.common.by import By


class NeedsQuestionsPage(BasePage):

    def is_title_matches(self):
        return "Administration | Organisation | Fact Find | Intelligent Office" == self.driver.title

    def click_add_needs_question_link(self):
        return self.click(Locators.ADD_NEEDS_QUESTION_LINK)

    def click_question_checkbox(self):
        return self.click(Locators.QUESTION_CHECKBOX)

    def click_delete_button(self):
        return self.click(Locators.DELETE_BUTTON)


class Locators(object):
    ADD_NEEDS_QUESTION_LINK = (By.CSS_SELECTOR, 'div.quicklinks-wrapper.group > ul > li > a')
    QUESTION_CHECKBOX = (
        By.XPATH,
        "//*[starts-with(@id, 'NeedsAndPrioritiesQuestionGrid')and contains(., 'colour')]/td[1]/input")
    DELETE_BUTTON = (By.ID, 'NeedsAndPrioritiesQuestionGrid_14')
