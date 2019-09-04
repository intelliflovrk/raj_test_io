from dsl.login_to_io import LogIn
from dsl.complete_factfind import BaseFactFindPage
from ioffice.clients.factfind.employment import EmploymentStage
from pfp.factfind.employment import EmploymentWizard
from pfp.factfind.profile import ProfilePage
from pfp.base import PFPBasePage
from pfp.factfind.your_profile_dialog import YourProfileDialogue
from pfp.factfind.you_and_your_family import YouAndYourFamily
from pfp.factfind.about_you_wizard import *
from pfp.factfind.your_family_wizard import YourFamilyWizard
from dsl.search import SearchClient
from dsl.login_to_pfp import LogIn as PFPLogin
from ioffice.clients.base import *
from ioffice.base import *
from ioffice.clients.factfind.profile import ProfileStage
from utils import *
import utils


class FactFind:
    def __init__(self, config):
        self.config = config
        self.wizard = {}

    def using_your_profile(self):
        PFPBasePage(self.config).click_view_profile_link()
        return FactFind._YourProfileDialog(ProfilePage(self.config), self)

    def logout_pfp(self):
        PFPBasePage(self.config).click_logout()
        return self

    def login_pfp(self):
        PFPLogin(self.config).navigate_to_login_page().login()
        return self

    def logout_io(self):
        IOBasePage(self.config).level1_menu().hover_over_user_navigation_menu().click_logout()
        return self

    def login_io(self):
        LogIn(self.config).login_as('gff_adviser_user')
        return self

    def open_client_fact_find(self):
        IoLevel3NavigationMenuSection(BaseClientPage(self.config)).click_factfind()
        return self

    def navigate_to_personal_tab(self):
        ProfileStage(self.config).click_personal_subtab()
        return self

    def update_date_of_birth(self):
        data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
        ProfileStage.Personal(self.config).fill_in_date_of_birth\
            ('/'.join([data["UPDATED_DOB_DATE"], data["UPDATED_DOB_MONTH"], data["UPDATED_DOB_YEAR"]]))\
            .click_save_button()

        return self

    def fill_in_middle_name(self):
        ProfileStage.Personal(self.config)\
            .fill_in_middle_name(utils.get_common_data(self.config)["test_data"]["gff_client_data"]["MIDDLE_NAME"])
        return self

    def update_marital_status(self):
        ProfileStage.Personal(self.config)\
            .select_marital_status(utils.get_common_data(self.config)["test_data"]["gff_client_data"]["MARITAL_STATUS"])\
            .click_save_button()
        return self

    def navigate_to_employment_tab(self):
        BaseFactFindPage(self.config).click_employment_tab()
        return self

    def navigate_to_dependants_tab(self):
        ProfileStage(self.config).click_dependants_subtab()
        return self

    def verify_personal_client_data_syncronized(self):
        data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
        personal = ProfileStage.Personal(self.config)
        assert personal.get_title_value() == data["Title"], "Title was not saved successfully"
        assert personal.get_gender_value() == data["Gender"], "Gender was not saved successfully"
        assert personal.get_date_of_birth_value() == \
            '/'.join([data["DOB_DATE"], data["DOB_MONTH"], data["DOB_YEAR"]]), "DoB was not saved successfully"
        assert personal.get_other_place_of_birth_value() == \
            data["PLACE_OF_BIRTH"], "Place of birth was not saved successfully"
        assert personal.get_nationality_value() == data["NATIONALITY"], "Nationality was not saved successfully"
        assert personal.is_uk_resident(), "UK Residency was not saved successfully"
        assert personal.are_you_in_good_health(), "Are you in good health option was not saved successfully"
        assert not personal.are_you_a_smoker(), "Are you a smoker option was not saved successfully"
        assert not personal.do_you_have_a_valid_will(), "Do you have a valid Will option was not saved successfully"
        return self

    def verify_dependants_data_syncronized(self):
        data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
        relationship_fullname = get_temp_data(self.config, "dependant_name")
        dependants = ProfileStage.Dependants(self.config)
        assert dependants.get_full_name_value() == relationship_fullname, "Full Name was not saved successfully"
        assert dependants.get_relationship_value() == data["RELATIONSHIP_TYPE"]

    def navigate_to_you_and_your_family(self):
        self.using_your_profile()\
            .start_fact_find_completion()\
            .using_you_and_your_family()
        return FactFind._YouAndYourFamily(self)

    def search_open_gff_client(self):
        SearchClient(self.config).quick_search_client(utils.get_common_data(self.config)["test_data"]["gff_client_data"]["fullname"])
        utils.update_temp_data(self.config, "client", 0, "id", BaseClientPage(self.config).get_client_id())
        return self

    def verify_employment_data_synchronized(self):
        actual_employment_data = utils.get_str_list_from_list_of_webelements(EmploymentStage(self.config).get_employment_rows_string())[0].split(' ')
        expected_employment_data = list(utils.get_common_data(self.config)["test_data"]["gff_employment_data"].values())
        assert all(item in actual_employment_data for item in expected_employment_data), "Employment record not synced successfully"
        return self

    class _YourProfileDialog:
        def __init__(self, current_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = YourProfileDialogue(current_page)

        def start_fact_find_completion(self):
            self.dialog.click_get_started()
            return FactFind._Profile(self.journey)

    class _Profile:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = ProfilePage(self.config)

        def using_you_and_your_family(self):
            self.page.click_you_and_your_family_link()
            return FactFind(self.config)._YouAndYourFamily(self.journey)

    class _YouAndYourFamily:
        def __init__(self, journey):
            self.journey = journey
            self.config = journey.config
            self.page = YouAndYourFamily(self.config)

        def using_about_you_wizard(self):
            self.page.click_about_you()
            return FactFind._YouAndYourFamily._AboutYouWizard(self.journey, AboutYouWizard(self.config))

        def using_your_family(self):
            self.page.click_your_family()
            return FactFind._YouAndYourFamily._YourFamilyWizard(self.journey, YourFamilyWizard(self.config))

        def using_employment_segment(self):
            self.page.click_employment()
            return FactFind._YouAndYourFamily._EmploymentWizard(self.journey, EmploymentWizard(self.config))

        class _AboutYouWizard:
            def __init__(self, journey, wizard):
                self.config = journey.config
                self.journey = journey
                self.wizard = wizard

            def add_basic_personal_details(self):
                data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
                title_and_gender = self.wizard.title_and_gender_stage()
                title_and_gender \
                    .click_title_option(data["Title"]) \
                    .click_gender_option(data["Gender"])
                date_of_birth = self.wizard.date_of_birth_stage()
                date_of_birth.goto_stage()
                date_of_birth.fill_in_date_of_birth_fields()
                place_of_birth = self.wizard.place_of_birth_stage()
                place_of_birth.goto_stage()
                place_of_birth.fill_in_place_of_birth(data["PLACE_OF_BIRTH"])
                nationality = self.wizard.nationality_stage()
                nationality.goto_stage()
                nationality \
                    .delete_nationality() \
                    .fill_in_nationality_field(data["NATIONALITY"])
                residence = self.wizard.residence_stage()
                residence.goto_stage()
                residence.click_residence_option(data["RESIDENCE"])
                health = self.wizard.health_stage()
                health.goto_stage()
                health \
                    .click_are_in_good_health_option(data["HEALTH_STATUS"]) \
                    .click_have_you_smoked_option(data["SMOKE_STATUS"])
                will = self.wizard.will_stage()
                will.goto_stage()
                will.click_will_status_option(data["WILL_STATUS"])
                photo = self.wizard.photo_stage()
                photo.goto_stage()
                self.wizard.click_next_button()
                review = self.wizard.review_stage()
                review.click_save_and_close_button()
                return FactFind._YouAndYourFamily(self.journey)

            def verify_personal_data_was_updated(self):
                data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
                review = self.wizard.click_review_button()
                assert review.get_middle_name_value() == data["MIDDLE_NAME"], "Middle Name was not updated"
                assert review.get_marital_status_value() == data["MARITAL_STATUS"], "Marital status was not updated"
                review.click_save_and_close_button()
                return self

        class _YourFamilyWizard:
            def __init__(self, journey, wizard):
                self.config = journey.config
                self.journey = journey
                self.wizard = wizard

            def add_dependant(self):
                data = utils.get_common_data(self.config)["test_data"]["gff_client_data"]
                relationship_name = fakedata.rand_firstname(self, "first_name") + \
                                    "_" + fakedata.rand_lastname(self, "last_name")
                utils.add_temp_data(self.config, "dependant_name", relationship_name)
                family_members = self.wizard.your_family_member_stage()
                family_members.click_add_family_member()
                relationship = self.wizard.relationship_type_stage()
                relationship.click_relationship_type_option(data["RELATIONSHIP_TYPE"])
                name = self.wizard.name_stage()
                name.goto_stage()
                name.fill_in_name_field(get_temp_data(self.config, "dependant_name"))
                date_of_birth = self.wizard.date_of_birth_stage()
                date_of_birth.goto_stage()
                living_with_you = self.wizard.living_with_you_stage()
                living_with_you.goto_stage()
                self.wizard.click_next_button()
                review = self.wizard.review_stage()
                review.click_save_and_close_button()
                family_members = self.wizard.your_family_member_stage()
                family_members \
                    .click_yes_button() \
                    .click_save_and_close_button()
                return self.journey

        class _EmploymentWizard:
            def __init__(self, journey, wizard):
                self.config = journey.config
                self.journey = journey
                self.wizard = wizard

            def add_current_employment_record(self):
                utils.add_temp_data(self.config, "client", {
                    "employment_data": utils.get_common_data(self.config)["test_data"]["gff_employment_data"]})
                data = utils.get_temp_data(self.config, "client")["employment_data"]
                data['occupation'] = data['occupation'] + fakedata.rand_text(5)
                data['employer_name'] = data['employer_name'] + fakedata.rand_text(5)
                self.wizard.click_add_current_employment_record()
                title = self.wizard.employment_title_stage()
                title.goto_stage()
                title.select_job_title(data['status'])
                occupation = self.wizard.occupation_stage()
                occupation.goto_stage()
                occupation.fill_in_occupation(data['occupation'])
                employer = self.wizard.employer_stage()
                employer.goto_stage()
                employer.fill_in_employer_name(data['employer_name'])
                start_date = self.wizard.date_stage()
                start_date.goto_stage()
                start_date.fill_in_start_date(data['start_date'].split('/')[0])\
                    .fill_in_start_month(data['start_date'].split('/')[1])\
                    .fill_in_start_year(data['start_date'].split('/')[2])
                income = self.wizard.income_stage()
                income.goto_stage()
                overtime = self.wizard.overtime_stage()
                overtime.goto_stage()
                bonus = self.wizard.bonus_stage()
                bonus.goto_stage()
                self.wizard.click_next_button()
                review = self.wizard.review_stage()
                review.click_save_and_close_button()
                return self

            def save_and_close(self):
                self.wizard.click_save_and_close()
                return self.journey






