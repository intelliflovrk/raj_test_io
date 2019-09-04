import time
import utils
from ioffice.admin.admin import AdministrationPage
from dsl.complete_factfind import CompleteFactFind
from ioffice.admin.organisation.base import BaseOrganisationPage
from ioffice.admin.organisation.factfind.base import BaseOrganisationFactFindPage
from ioffice.admin.organisation.factfind.needs_questions import NeedsQuestionsPage
from ioffice.admin.organisation.factfind.add_needs_question_dialog import AddNeedsQuestionDialog
from ioffice.clients.client_dashboard import ClientDashboardPage


class SetupNeedsAndPrioritiesQuestions(CompleteFactFind):

    def __init__(self, config):
        super().__init__(config)
        self.wizard = {}
        self.page = {}

    def navigate_to_needs_questions(self):
        ClientDashboardPage(self.config).level1_menu().hover_over_navigation_menu().click_administration()
        AdministrationPage(self.config).level2_menu().click_organisation()
        BaseOrganisationPage(self.config).level3_menu().click_factfind()
        BaseOrganisationFactFindPage(self.config).level4_menu().click_needs_questions()
        assert NeedsQuestionsPage(
            self.config).is_title_matches(), "Title does not match the Needs Questions page"
        self.needs_questions_journey = SetupNeedsAndPrioritiesQuestions._NeedsQuestionsJourney(self)
        return self.needs_questions_journey

    def verify_factfind_documents_downloaded(self):
        time.sleep(5)
        url = utils.get_download_folder(self.config)
        utils.verify_file_is_downloaded(url, "Fact Find.pdf")
        return self

    class _NeedsQuestionsJourney:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.needs_questions = NeedsQuestionsPage(self.config)

        def add_needs_question(self):
            NeedsQuestionsPage(self.config).click_add_needs_question_link()
            return self

        def fill_needs_question_form(self):
            needs_questions = AddNeedsQuestionDialog(self.needs_questions)
            data = utils.get_common_data(self.config)["test_data"]["needs_questions_setup_details"]
            needs_questions.page.fill_in_form(data, needs_questions)
            needs_questions.click_group_in_profile_checkbox()
            needs_questions.click_save_button()
            return self.journey

        def delete_question(self):
            NeedsQuestionsPage(self.config).click_question_checkbox().click_delete_button().\
                click_ok_in_browser_confirmation_dialog()
            return self
