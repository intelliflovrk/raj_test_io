from dsl.search import SearchClient
from fakedata import *
from ioffice.clients.base import BaseClientPage
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.factfind.add_remove_partner_dialog import AddRemovePartnerDialog
from ioffice.clients.factfind.protection_buildings_contents import BuildingsContentsTab
from ioffice.clients.factfind.protection_existing_provision import ExistingProvisionTab
from ioffice.clients.factfind.protection_income import IncomeProtectionTab
from ioffice.clients.factfind.protection_life_critical import LifeCriticalTab
from ioffice.clients.factfind.linked_documents_dialog import LinkedDocumentsDialog
from ioffice.clients.factfind.protection_summary import SummaryProtectionSubTab
from ioffice.clients.factfind.view_pdfs_dialog import ViewPDFSDialog
from ioffice.clients.documents.documents import ClientDocumentsPage
from ioffice.clients.factfind.profile import ProfileStage
from ioffice.clients.factfind.employment import EmploymentStage
from ioffice.clients.factfind.assets_and_liabilities import AssetLiabilitiesStage
from ioffice.clients.factfind.budget import BudgetStage
from ioffice.clients.factfind.retirement import RetirementStage
from ioffice.clients.factfind.estate_planning import EstatePlanningStage
from ioffice.clients.factfind.summary import SummaryStage
from ioffice.clients.opportunities.opportunities import OpportunitiesPage
from ioffice.clients.factfind.mortgage import MortgageStage
from ioffice.clients.factfind.protection_tab import *
from utils import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CompleteFactFind(SearchClient):

    def __init__(self, config):
        super().__init__(config)
        self.wizard = {}
        self.page = {}

    def go_to_fact_find(self):
        clientdashboard = ClientDashboardPage(self.config)
        self.client_id = BaseClientPage(self.config).get_client_id()
        clientdashboard.level3_menu().click_factfind()
        factfind = CompleteFactFind._FactFindJourney(self, BaseFactFindPage(self.config))
        factfinddashboard = BaseFactFindPage(self.config)
        self.factfind_ref = factfinddashboard._get_factfind_ref()
        self.factfind = CompleteFactFind._FactFindJourney(self, BaseFactFindPage(self.config))
        return factfind

    def verify_pdf_contains_first_life_records(self):
        time.sleep(30)
        get_pdf_outline(self, "Fact Find.pdf")
        assert get_temp_data(self.config, "client")["person"]["firstName"] + ' ' + get_temp_data(self.config, "client")["person"]["lastName"] in str(self.pdf_outline[0]), "The given name is not present in the PDF outline."
        return self

    def using_view_pdfs_dialog(self):
        profile = ProfileStage(self.config)
        profile.factfind_actions_menu().hover_over_factfind_actions_menu().click_view_pdfs()
        self.page = profile
        dialog = CompleteFactFind._ViewPDFs(self.client_id, self.factfind_ref, self.page, self)
        return dialog

    def using_documents_section(self):
        ClientDashboardPage(self.config).level3_menu().click_documents()
        return CompleteFactFind._VerifyDocuments(self)

    def using_opportunities_section(self):
        clientdashboard = ClientDashboardPage(self.config)
        clientdashboard.level3_menu().click_opportunities()
        documents = CompleteFactFind._VerifyOpportunity(self)
        return documents

    def navigate_to_dashboard_tab(self):
        BaseClientPage(self.config).level3_menu().click_dashboard()
        return self

    class _FactFindJourney:
        def __init__(self, journey, factfind):
            self.config = journey.config
            self.journey = journey
            self.factfind = BaseFactFindPage(self.config)
            assert self.factfind.is_title_matches(), "Title does not match the factfind page"

        def navigate_to_existing_protection_provision_tab(self):
            base_fact_find = BaseFactFindPage(self.config)
            ProfileStage(self.config).click_select_protection()
            base_fact_find.click_save_button()
            ProtectionTab(self.config).click_protection_tab().click_existing_provision_sub_tab()
            ExistingProvisionTab(self.config).click_have_existing_policies_yes_radio_button()
            base_fact_find.click_save_button()
            return self

        def using_add_remove_partner_wizard(self):
            profile = ProfileStage(self.config)
            profile.factfind_actions_menu().hover_over_factfind_actions_menu()
            profile.factfind_actions_menu().click_add_remove_partner()
            return self

        def add_partner(self):
            add_partner_dialog = AddRemovePartnerDialog(self.factfind)
            self.journey.secondlife_fullname = add_partner_dialog.get_partner_name()
            add_partner_dialog.click_add_first_partner()
            return self

        def remove_partner(self):
            add_partner_dialog = AddRemovePartnerDialog(self.factfind)
            self.journey.secondlife_fullname = add_partner_dialog.get_partner_name()
            add_partner_dialog.click_remove_first_partner()
            utils.switch_and_accept_alert(self.config)
            return self

        def verify_client_and_partner_present_on_client_bar(self):
            assert get_temp_data(self.config, "client")["person"]["firstName"] + ' ' + get_temp_data(self.config, "client")["person"]["lastName"] in BaseClientPage(
                self.config).get_client_bar_info(), "First life name is not present in client bar."
            assert self.journey.secondlife_fullname in BaseClientPage(
                self.config).get_client_bar_info(), "Second life name is not present in client bar."
            return self

        def navigate_to_profile_personal_sub_tab(self):
            ProfileStage(self.config).click_personal_subtab()
            return self

        def verify_second_life_present_on_personal_tab(self):
            assert get_temp_data(self.config, "client")["person"]["firstName"] + ' ' + get_temp_data(self.config, "client")["person"]["lastName"] in ProfileStage.Personal.get_first_life_full_name(
                self.config), "First life name is not present on Personal sub tab."
            assert self.journey.secondlife_fullname in ProfileStage.Personal.get_second_life_full_name(
                self.config), "Second life name is not present on Personal sub tab."
            return self

        def navigate_to_employment_tab(self):
            BaseFactFindPage(self.config).click_employment_tab()
            return self

        def verify_second_life_present_on_employment_tab(self):
            assert get_temp_data(self.config, "client")["person"]["firstName"] + ' ' + get_temp_data(self.config, "client")["person"]["lastName"] in EmploymentStage.get_first_life_full_name(
                self.config), "First life name is not present on Employment tab."
            assert self.journey.secondlife_fullname in EmploymentStage.get_second_life_full_name(
                self.config), "Second life name is not present on Employment tab."
            return self.journey

        def navigate_to_protection_tab(self):
            ProfileStage(self.config).click_select_protection()
            BaseFactFindPage(self.config).click_save_button()
            ProtectionTab(self.config).click_protection_tab()
            return self

        def navigate_to_needs_and_priorities_tab(self):
            BaseFactFindPage(self.config).click_profile_tab()
            ProfileStage(self.config).click_needs_and_priorities_subtab()
            return self

        def navigate_to_risk_tab(self):
            BaseFactFindPage(self.config).click_profile_tab()
            ProfileStage(self.config).click_risk_subtab()
            return self

        def fill_in_risk_question_category(self):
            ProfileStage.Risk(self.config).fill_in_form(
                get_common_data(self.config)["test_data"]["fact_find_data"]["risk_question_category"],
                ProfileStage.Risk(self.config))
            return self

        def verify_risk_warning_message(self):
            assert ProfileStage.Risk(self.config).get_warning_message() == \
                   "Please review the Risk Question Consistency section below.", "Warning message not found"
            return self

        def save_generated_risk_profile(self):
            self.config.risk_profile = ProfileStage.Risk(self.config).get_generated_risk_profile()
            return self

        def verify_save_button_disabled(self):
            assert "disabled" in ProfileStage.Risk(self.config).get_save_button_attribute(), "Save button not disabled"
            return self

        def fill_in_risk_notes_and_save(self):
            ProfileStage.Risk(self.config).fill_in_risk_notes_field()
            ProfileStage(self.config).click_save_button()
            return self

        def verify_risk_notes_saved(self):
            assert ProfileStage.Risk(self.config) \
                       .get_risk_notes_value() == utils.get_common_data(self.config)["basic_data"]["basic_text"][
                       "BASIC_TEXT"], "Risk notes not saved successfully"
            return self

        def clear_risk_subtab_data(self):
            self.navigate_to_risk_tab()
            ProfileStage.Risk(self.config).fill_in_form(
                get_common_data(self.config)["test_data"]["fact_find_data"]
                ["risk_clear_data"], ProfileStage.Risk(self.config))
            ProfileStage(self.config).click_save_button()
            return self

        def navigate_to_risk_replay_tab(self):
            BaseFactFindPage(self.config).click_profile_tab()
            ProfileStage(self.config).click_risk_replay_subtab()
            return self

        def verify_generated_risk_profile(self):
            assert ProfileStage.RiskReplay(self.config).get_generated_risk_profile() == \
                   self.config.risk_profile, "Generated risk profile not matching"
            return self

        def click_risk_profile_radio_button_no(self):
            ProfileStage.RiskReplay(self.config).click_risk_profile_radio_button_no()
            return self

        def verify_chosen_risk_profile_presence(self):
            assert ProfileStage.RiskReplay(self.config).get_chosen_risk_profile() == \
                   "Chosen Risk Profile", "Chosen Risk Profile not present"
            return self

        def fill_in_risk_replay_notes_and_save(self):
            ProfileStage.RiskReplay(self.config).fill_in_risk_replay_notes()
            ProfileStage(self.config).click_save_button()
            return self

        def verify_risk_replay_notes_saved(self):
            assert ProfileStage.RiskReplay(self.config) \
                       .get_risk_replay_notes_value() == get_common_data(self.config)["basic_data"]["basic_text"][
                       "BASIC_TEXT"], "Risk Replay notes not saved successfully"
            return self

        def verify_saved_needs_question_is_present(self):
            data = utils.get_common_data(self.config)["test_data"]["needs_questions_setup_details"]
            assert ProfileStage.NeedsAndPriorities(self.config).get_needs_and_priorities_question() == data[
                "QUESTION_TEXT"], "Needs & Priorities question not found"
            return self.journey

        def clear_risk_replay_subtab_data(self):
            self.navigate_to_risk_replay_tab()
            ProfileStage.RiskReplay(self.config) \
                .click_risk_profile_radio_button_yes() \
                .clear_in_risk_replay_notes() \
                .click_save_button()
            return self

        def clear_need_and_priorities_answer(self):
            ProfileStage.NeedsAndPriorities(
                self.config).clear_needs_and_priorities_answer().press_backspace_on_field()
            BaseFactFindPage(self.config).click_save_button()
            return self

        def fill_need_and_priorities_details(self):
            ProfileStage.NeedsAndPriorities(self.config).complete_needs_and_priorities_answer()
            BaseFactFindPage(self.config).click_save_button()
            return self.journey

        def add_life_critical_illness(self):
            ProtectionTab(self.config).click_life_critical_illness_tab()
            self.fill_in_life_critical_form()
            self.save_form()
            return self

        def add_income_protection(self):
            ProtectionTab(self.config).click_income_protection_sub_tab()
            self.fill_in_income_protection_form()
            self.save_form()
            return self

        def add_buildings_contents(self):
            ProtectionTab(self.config).click_buildings_contents_tab()
            self.fill_in_buildings_contents_form()
            self.save_form()
            return self

        def select_existing_building_insurance(self, param):
            if param == "true":
                BuildingsContentsTab(self.config).click_existing_building_yes_radio_button()
            else:
                BuildingsContentsTab(self.config).click_existing_building_no_radio_button()

        def select_exisitng_content_insurance(self, param):
            if param == "true":
                BuildingsContentsTab(self.config).click_existing_content_insurance_yes_radio_button()
            else:
                BuildingsContentsTab(self.config).click_existing_content_insurance_no_radio_button()

        def select_buy_to_let_properties(self, param, insurance):
            if param == "true":
                BuildingsContentsTab(self.config).click_buy_to_let_yes_radio_button()
                self.select_sufficient_insurance(insurance)
            else:
                BuildingsContentsTab(self.config).click_buy_to_let_no_radio_button()

        def select_sufficient_insurance(self, param):
            if param == "true":
                BuildingsContentsTab(self.config).click_sufficient_insurance_yes_radio_button()
            else:
                BuildingsContentsTab(self.config).click_sufficient_insurance_no_radio_button()

        def select_sufficient_protection(self, param):
            if param == "true":
                BuildingsContentsTab(self.config).click_sufficient_protection_yes_radio_button()
            else:
                BuildingsContentsTab(self.config).click_sufficient_protection_no_radio_button()

        def select_mortgage_debt_radio_button(self, param):
            if param == "true":
                LifeCriticalTab(self.config).click_mortgage_and_debt_yes_radio_button()
            elif param == "false":
                LifeCriticalTab(self.config).click_mortgage_and_debt_no_radio_button()
            else:
                LifeCriticalTab(self.config).click_mortgage_and_debt_not_applicable_radio_button()
            return self

        def select_life_standards_critical_illness_radio_button(self, param):
            if param == "true":
                LifeCriticalTab(self.config).click_life_standards_critical_illness_yes_radio_button()
            else:
                LifeCriticalTab(self.config).click_life_standards_critical_illness_no_radio_button()
            return self

        def select_life_standards_death_radio_button(self, param):
            if param == "true":
                LifeCriticalTab(self.config).click_life_standards_death_yes_radio_button()
            elif param == "fasle":
                LifeCriticalTab(self.config).click_life_standards_death_no_radio_button()
            else:
                LifeCriticalTab(self.config).click_life_standards_death_not_applicable_radio_button()

        def select_cost_of_protection_radio_button(self, param):
            if param == "true":
                LifeCriticalTab(self.config).click_cost_of_protection_yes_radio_button()
            else:
                LifeCriticalTab(self.config).click_cost_of_protection_no_radio_button()
            return self

        def select_unable_to_work_illness(self, param):
            if param == "true":
                IncomeProtectionTab(self.config).click_unable_to_work_illness_yes_radio_button()
            elif param == "false":
                IncomeProtectionTab(self.config).click_unable_to_work_illness_no_radio_button()
            else:
                IncomeProtectionTab(self.config).click_unable_to_work_illness_not_applicable_radio_button()

        def select_unable_to_work_unemployment(self, param):
            if param == "true":
                IncomeProtectionTab(self.config).click_unable_to_work_unemployment_yes_radio_button()
            elif param == "false":
                IncomeProtectionTab(self.config).click_unable_to_work_unemployment_no_radio_button()
            else:
                IncomeProtectionTab(self.config).click_unable_to_work_unemployment_not_applicable_radio_button()

        def fill_in_income_protection_form(self):
            income_protection_tab = IncomeProtectionTab(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_income_protection_form"]
            self.select_unable_to_work_illness(data["unable_to_work_illness"])
            self.select_unable_to_work_unemployment(data["unable_to_work_unemployment"])
            income_protection_tab.fill_in_form(data, income_protection_tab)
            return self

        def fill_in_life_critical_form(self):
            life_critical_tab = LifeCriticalTab(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_life_critical_form"]
            self.select_mortgage_debt_radio_button(data["is_mortgage_debt_cleared"])
            self.select_life_standards_critical_illness_radio_button(data["life_standards_critical_illness"])
            self.select_life_standards_death_radio_button(data["life_standards_death"])
            self.select_cost_of_protection_radio_button(data["cost_of_protection"])
            life_critical_tab.fill_in_form(data, life_critical_tab)
            return self

        def fill_in_buildings_contents_form(self):
            buildings_contents_tab = BuildingsContentsTab(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_building_content_form"]
            self.select_existing_building_insurance(data["existing_building_insurance"])
            self.select_exisitng_content_insurance(data["existing_content_insurance"])
            self.select_buy_to_let_properties(data["buy_to_let_properties"],
                                              data["sufficient_building_insurance"])
            self.select_sufficient_protection(data["sufficient_protection"])
            buildings_contents_tab.fill_in_form(data, buildings_contents_tab)
            return self

        def save_form(self):
            BaseFactFindPage(self.config).click_save_button()
            return self

        def verify_buildings_contents_form_was_saved(self):
            buildings_contents_tab = BuildingsContentsTab(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_building_content_form"]
            self.verify_existing_building_radio_button(data["existing_building_insurance"])
            self.verify_existing_contents_insurance_radio_button(data["existing_content_insurance"])
            self.verify_buy_to_let_radio_button(data["buy_to_let_properties"])
            self.verify_sufficient_building_insurance_radio_button(data["sufficient_building_insurance"])
            self.verify_sufficient_protection_radio_button(data["sufficient_protection"])
            assert buildings_contents_tab.get_how_to_address_value() == data["ADDRESS_THIS_TEXTFIELD"], \
                "How do you want to address this textbox content wasn't saved succesfully."
            assert buildings_contents_tab.get_when_do_you_want_to_review_value() == data["WHEN_DO_YOU_WANT_TO_REVIEW"], \
                "When do you want to review this textbox content wasn't saved succesfully."
            assert buildings_contents_tab.get_reason_if_no_value() == data["REASON_FOR_REVIEW"], \
                "Reason if no testbox content wasn't saved succesfully."
            return self

        def verify_income_protection_form(self):
            income_protection_tab = IncomeProtectionTab(self.config)

            data = get_common_data(self.config)["test_data"]["fact_find_income_protection_form"]

            self.verify_unable_to_work_illness_radio_button(data["unable_to_work_illness"])
            self.verify_unable_to_work_unemployment_radio_button(data["unable_to_work_unemployment"])
            assert income_protection_tab.get_impact_on_customer_value() == data["IMPACT_ON_CUSTOMER"], \
                "Impact on customer textbox content wasn't saved succesfully."
            assert income_protection_tab.get_impact_on_dependants_value() == data["IMPACT_ON_DEPENDANTS"], \
                "Impact on dependants textbox content wasn't saved succesfully."
            assert income_protection_tab.get_address_this_value() == data["ADDRESS_THIS_TEXTFIELD"], \
                "Address this textbox content wasn't saved succesfully."
            assert income_protection_tab.get_not_reviewing_reason_value() == data["REASON_NOT_REVIEW"], \
                "Impact on customer textbox content wasn't saved succesfully."
            return self

        def verify_life_critical_form(self):
            life_critical_tab = LifeCriticalTab(self.config)

            data = get_common_data(self.config)["test_data"]["fact_find_life_critical_form"]

            self.verify_is_mortgage_debt_cleared_radio_button(data["is_mortgage_debt_cleared"])
            self.verify_life_standards_critical_illness_radio_button(data["life_standards_critical_illness"])
            self.verify_life_standards_death_radio_button(data["life_standards_death"])
            self.verify_cost_of_protection_radio_button(data["cost_of_protection"])

            assert life_critical_tab.get_impact_on_customer_value() == data["IMPACT_ON_CUSTOMER"], \
                "Impact on customer textbox content wasn't saved succesfully."
            assert life_critical_tab.get_impact_on_dependants_value() == data["IMPACT_ON_DEPENDANTS"], \
                "Impact on dependants textbox content wasn't saved succesfully."
            assert life_critical_tab.get_address_this_value() == data["ADDRESS_THIS_TEXTFIELD"], \
                "Address this testbox content wasn't saved succesfully."
            assert life_critical_tab.get_reason_to_not_review_value() == data["REASON_TO_REVIEW"], \
                "Reason to not review testbox content wasn't saved succesfully."
            return self

        def verify_unable_to_work_illness_radio_button(self, param):
            if param == "true":
                assert IncomeProtectionTab(self.config).get_unable_to_work_illness_yes_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            elif param == "false":
                assert IncomeProtectionTab(self.config).get_unable_to_work_illness_no_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            else:
                assert IncomeProtectionTab(self.config).get_unable_to_work_illness_not_applicable_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            return self

        def verify_unable_to_work_unemployment_radio_button(self, param):
            if param == "true":
                assert IncomeProtectionTab(self.config).get_unable_to_work_unemployment_yes_radio_button_state(), \
                    "Unable to work unemployment radio button wasn't saved successfully."
            elif param == "false":
                assert IncomeProtectionTab(self.config).get_unable_to_work_unemployment_no_radio_button_state(), \
                    "Unable to work unemployment radio button wasn't saved successfully."
            else:
                assert IncomeProtectionTab(
                    self.config).get_unable_to_work_unemployment_not_applicable_radio_button_state(), \
                    "Unable to work unemployment radio button wasn't saved successfully."
            return self

        def verify_is_mortgage_debt_cleared_radio_button(self, param):
            if param == "true":
                assert LifeCriticalTab(self.config).get_is_mortgage_debt_cleared_yes_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            elif param == "false":
                assert LifeCriticalTab(self.config).get_is_mortgage_debt_cleared_no_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            else:
                assert LifeCriticalTab(self.config).get_is_mortgage_debt_cleared_not_applicable_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            return self

        def verify_life_standards_death_radio_button(self, param):
            if param == "true":
                assert LifeCriticalTab(self.config).get_life_standards_death_yes_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            elif param == "false":
                assert LifeCriticalTab(self.config).get_life_standards_death_no_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            else:
                assert LifeCriticalTab(self.config).get_life_standards_death_not_applicable_radio_button_state(), \
                    "Is mortgage debt cleared radio button wasn't saved successfully."
            return self

        def verify_life_standards_critical_illness_radio_button(self, param):
            if param == "true":
                assert LifeCriticalTab(self.config).get_life_standards_critical_illness_yes_radio_button_state(), \
                    "Life standards radio button wasn't saved successfully."
            else:
                assert LifeCriticalTab(self.config).get_life_standards_critical_illness_no_radio_button_state(), \
                    "Life standards radio button wasn't saved successfully."
            return self

        def verify_cost_of_protection_radio_button(self, param):
            if param == "true":
                assert LifeCriticalTab(self.config).get_cost_of_protection_yes_radio_button_state(), \
                    "Life standards radio button wasn't saved successfully."
            else:
                assert LifeCriticalTab(self.config).get_cost_of_protection_no_radio_button_state(), \
                    "Life standards radio button wasn't saved successfully."
            return self

        def verify_existing_building_radio_button(self, param):
            if param == "true":
                assert BuildingsContentsTab(self.config).get_existing_building_insurance_yes_radio_button_state(), \
                    "Existing Building Radio button wasn't saved successfully."
            else:
                assert BuildingsContentsTab(self.config).get_existing_building_insurance_no_radio_button_state(), \
                    "Existing Building Radio button wasn't saved successfully."
            return self

        def verify_existing_contents_insurance_radio_button(self, param):
            if param == "true":
                assert BuildingsContentsTab(self.config).get_existing_contents_yes_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            else:
                assert BuildingsContentsTab(self.config).get_existing_contents_no_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            return self

        def verify_buy_to_let_radio_button(self, param):
            if param == "true":
                assert BuildingsContentsTab(self.config).get_buy_to_let_yes_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            else:
                assert BuildingsContentsTab(self.config).get_buy_to_let_no_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            return self

        def verify_sufficient_building_insurance_radio_button(self, param):
            if param == "true":
                assert BuildingsContentsTab(self.config).get_sufficient_building_insurance_yes_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            else:
                assert BuildingsContentsTab(self.config).get_sufficient_building_insurance_no_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            return self

        def verify_sufficient_protection_radio_button(self, param):
            if param == "true":
                assert BuildingsContentsTab(self.config).get_sufficient_protection_yes_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            else:
                assert BuildingsContentsTab(self.config).get_sufficient_protection_no_radio_button_state(), \
                    "Existing Content Insurance Radio button wasn't saved successfully."
            return self

        def add_term_protection_plan(self):
            self.add_contract(
                get_common_data(self.config)["test_data"]["fact_find_add_existing_provision_term_protection"])
            return self

        def add_income_protection_plan(self):
            self.add_contract(
                get_common_data(self.config)["test_data"]["fact_find_add_existing_provision_income_protection"])
            return self

        def add_whole_of_life_plan(self):
            self.add_contract(
                get_common_data(self.config)["test_data"]["fact_find_add_existing_provision_whole_of_life"])
            return self

        def add_family_income_benefit_plan(self):
            self.add_contract(
                get_common_data(self.config)["test_data"]["fact_find_add_existing_provision_family_income_benefit"])
            return self

        def add_contract(self, data):
            existing_provision_tab = ExistingProvisionTab(self.config)
            existing_provision_tab.click_add_protection_plan()
            existing_provision_tab.fill_in_form(data, existing_provision_tab) \
                .click_save_existing_protection_plan()
            return self

        def verify_contracts_added(self):
            data = ExistingProvisionTab(self.config).get_existing_protection_plans_str_list()
            assert utils.is_string_present(data, get_common_data(self.config)["test_data"][
                "fact_find_add_existing_provision_term_protection"][
                "TYPE_OF_CONTRACT"]), "Term Protection wasn't saved successfully"
            assert utils.is_string_present(data, get_common_data(self.config)["test_data"][
                "fact_find_add_existing_provision_family_income_benefit"][
                "TYPE_OF_CONTRACT"]), "Family Income Benefit Protection wasn't saved successfully"
            assert utils.is_string_present(data, get_common_data(self.config)["test_data"][
                "fact_find_add_existing_provision_whole_of_life"][
                "TYPE_OF_CONTRACT"]), "Whole of Life wasn't saved successfully"
            assert utils.is_string_present(data, get_common_data(self.config)["test_data"][
                "fact_find_add_existing_provision_income_protection"][
                "TYPE_OF_CONTRACT"]), "Income Protection wasn't saved successfully"
            return self

        def verify_summary_screen(self):
            ProtectionTab(self.config).click_protection_summary_sub_tab()
            assert SummaryProtectionSubTab(self.config).get_life_cover_sum() == get_common_data(
                self.config)["test_data"]["fact_find_add_existing_provision_term_protection"][
                "LIFE_COVER_SUM"], "Life cover sum wasn't saved successfully"
            assert SummaryProtectionSubTab(self.config).get_illness_cover_field() == get_common_data(
                self.config)["test_data"]["fact_find_add_existing_provision_term_protection"][
                "CRITICAL_ILLNESS_SUM"], "Critical Illness cover sum wasn't saved successfully"
            ProtectionTab(self.config).click_existing_provision_sub_tab()
            return self

        def tick_all_agreement_statements(self):
            dpa_statements = WebDriverWait(self.config.driver, self.factfind.TIMEOUT).until(
                EC.presence_of_all_elements_located(
                    ProfileStage.DataProtection.Locators.DPA_ALL_CHECKBOXES))
            for i in range(1, len(dpa_statements) + 1):
                self.factfind.driver.find_element(
                    By.ID, ProfileStage.DataProtection.Locators.FIRST_DPA_CHECKBOX.format(i)) \
                    .click()
            return self

        def fill_up_advice_areas_tab(self):
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            BaseFactFindPage(self.config).click_profile_tab()
            ProfileStage.AdviceAreas(self.config).click_add_button()\
                .select_document_type(data["DOCUMENT_TYPE"]["COMBINED_DISCLOSURE_DOCUMENTS"])\
                .fill_in_date_issued(data["DATE_ISSUED"]).click_save_button()\
                .click_add_button()\
                .select_document_type(data["DOCUMENT_TYPE"]["KEY_FACTS_ABOUT_SERVICES"])\
                .click_save_button()
            return self

        def fill_up_data_protection_tab(self):
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            ProfileStage(self.config)\
                .click_data_protection_subtab()
            ProfileStage.DataProtection(self.config)\
                .click_add_button()
            self.tick_all_agreement_statements()
            ProfileStage.DataProtection(self.config)\
                .fill_in_agreement_date(data["DATE_ISSUED"])\
                .click_save_button()
            return self

        def fill_up_personal_tab(self):
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            ProfileStage(self.config).click_personal_subtab()
            ProfileStage.Personal(self.config)\
                .select_marital_status(data["MARITAL_STATUS"])\
                .fill_in_national_insurance_number(data["NATIONAL_INSURANCE_NUMBER"])\
                .select_uk_residency_checkbox()\
                .click_save_button()

        def fill_up_contact_tab(self):
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            profile = ProfileStage(self.config)
            profile_contactdetails = ProfileStage.ContactDetails(self.config)
            profile.click_contact_details_subtab()
            profile_contactdetails.click_add_contact_button()
            profile_contactdetails.fill_in_contact_value_field(data["CONTACT_VALUE"])
            profile_contactdetails.click_save_button()
            profile_contactdetails.click_add_professional_contact_button()
            profile_contactdetails.fill_in_form(data["professional_contact_form"], profile_contactdetails)
            profile_contactdetails.click_save_button()

        def fill_up_dependants_tab(self):
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            ProfileStage(self.config)\
                .click_dependants_subtab()
            ProfileStage.Dependants(self.config)\
                .click_add_button()\
                .fill_in_full_name(rand_firstname(self, "first_name"))\
                .fill_in_date_of_birth(data["DATE_ISSUED"])\
                .click_save_button()
            return self

        def add_profile_details(self):
            BaseFactFindPage(self.config)\
                .click_profile_tab()
            self.fill_up_advice_areas_tab()
            self.fill_up_data_protection_tab()
            self.fill_up_personal_tab()
            self.fill_up_contact_tab()
            self.fill_up_dependants_tab()
            return self

        def add_employment_details(self):
            factfind = BaseFactFindPage(self.config)
            factfind.click_employment_tab()
            employment = EmploymentStage(self.config)
            employment.click_add_button()
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            employment.select_employment_status(data["EMPLOYMENT_STATUS"])
            employment.fill_in_form(data["employment_details_form"], employment)
            employment.click_save_button()
            return self

        def add_assets_liability_details(self):
            common_data = get_common_data(self.config)
            factfind = BaseFactFindPage(self.config)
            factfind.click_asset_and_liabilities_tab()
            assetliabilities = AssetLiabilitiesStage(self.config)
            assetliabilities.click_assets_subtab()
            assetliabilities_assets = AssetLiabilitiesStage.Assets(self.config)
            assetliabilities_assets.click_yes_radiobutton()
            assetliabilities.click_save_button()
            assetliabilities_assets.click_add_button()
            assetliabilities_assets.fill_in_description_field(common_data["basic_data"]["basic_text"]["BASIC_TEXT"])
            assetliabilities_assets.fill_in_original_value_field(
                common_data["basic_data"]["basic_integer"]["BASIC_INTEGER"])
            assetliabilities_assets.click_save_button()
            assetliabilities.click_liabilities_subtab()
            assetliabilities_liabilities = AssetLiabilitiesStage.Liabilities(self.config)
            assetliabilities_liabilities.click_yes_radiobutton()
            assetliabilities.click_save_button()
            assetliabilities_liabilities.click_add_button()
            assetliabilities_liabilities.select_liability_category_status(
                common_data["test_data"]["fact_find_data"]["LIABILITY_CATEGORY"])
            assetliabilities_liabilities.fill_in_description_field(
                common_data["basic_data"]["basic_text"]["BASIC_TEXT"])
            assetliabilities_liabilities.fill_in_original_amount_field(
                common_data["basic_data"]["basic_integer"]["BASIC_INTEGER"])
            assetliabilities_liabilities.click_save_button()
            return self

        def navigate_to_budget(self):
            BaseFactFindPage(self.config).click_budget_tab()
            return self

        def navigate_to_income(self):
            BudgetStage(self.config).click_income_subtab()
            return self

        def navigate_to_expenditure(self):
            BudgetStage(self.config).click_expenditure_subtab()
            return self

        def navigate_to_monthly_affordability(self):
            BudgetStage(self.config).click_monthly_affordability_subtab()
            return self

        def add_budget_income_and_expenditure_details(self):
            self.navigate_to_budget().navigate_to_income().add_budget_income_details()
            self.navigate_to_expenditure().add_budget_detailed_expenditure_details()
            return self

        def add_budget_income_details(self):
            budget_income = BudgetStage.Income(self.config)
            budget_income.click_add_button()
            self.fill_income_details_form()
            return self

        def add_budget_detailed_expenditure_details(self):
            budget_expenditure = BudgetStage.Expenditure(self.config)
            budget_expenditure.click_expenditure_yes_button()
            test_data = get_common_data(self.config)["test_data"]["fact_find_data"]
            budget_expenditure.fill_in_form(test_data["budget_expenditure_form"], budget_expenditure)
            budget_expenditure.click_save_button()
            return self

        def add_budget_basic_expenditure_details(self):
            budget_expenditure = BudgetStage.Expenditure(self.config)
            budget_expenditure.click_expenditure_no_button().click_save_button()
            data = get_common_data(self.config)["test_data"]["budget_total_net_monthly_expenditure"]
            budget_expenditure.fill_in_total_net_monthly_expenditure_field(
                data["TOTAL_NET_MONTHLY_EXPENDITURE"])
            budget_expenditure.click_save_button()
            return self

        def fill_income_details_form(self):
            income = BudgetStage.Income(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_income_details_form"]
            for i in data:
                income.fill_in_field(income.Locators.__dict__.get(i), data[i])
            income.click_save_button()
            return self

        def verify_income_monthly_total_is_calculated(self):
            data = get_common_data(self.config)["test_data"]["fact_find_income_monthly_total"]
            assert BudgetStage.Income(self.config).get_monthly_total() == data[
                "MONTHLY_TOTAL"], "Monthly total is incorrect"
            return self

        def verify_expenditure_monthly_total_is_calculated(self):
            data = get_common_data(self.config)["test_data"]["budget_expenditure_total_monthly_amount"]
            assert BudgetStage.Expenditure(self.config).get_total_monthly_expenditure() == data[
                "TOTAL_MONTHLY_HOUSEHOLD_EXPENDITURE"], "Monthly expenditure total is incorrect"
            return self

        def verify_monthly_income_is_calculated(self):
            data = get_common_data(self.config)["test_data"]["fact_find_income_monthly_total"]
            assert BudgetStage.MonthlyExpenditure(self.config).get_total_monthly_income() == data[
                "MONTHLY_TOTAL"], "Total monthly income is incorrect"
            return self

        def verify_net_monthly_expenditure_is_calculated(self):
            data = get_common_data(self.config)["test_data"]["budget_total_net_monthly_expenditure"]
            assert BudgetStage.MonthlyExpenditure(self.config).get_total_monthly_expenditure() == data[
                "TOTAL_NET_MONTHLY_EXPENDITURE"], "Total monthly expenditure is incorrect"
            return self

        def verify_monthly_disposable_income_is_calculated(self):
            data = get_common_data(self.config)["test_data"]["budget_total_monthly_disposable_income"]
            assert BudgetStage.MonthlyExpenditure(self.config).get_total_monthly_disposable_income() == data[
                "TOTAL_MONTHLY_DISPOSABLE_INCOME"], "Total monthly disposable income is incorrect"
            return self

        def verify_budget_affordability_calculations(self):
            self.navigate_to_income().verify_income_monthly_total_is_calculated()
            self.navigate_to_expenditure().verify_expenditure_monthly_total_is_calculated()
            self.navigate_to_monthly_affordability().verify_monthly_income_is_calculated(). \
                verify_net_monthly_expenditure_is_calculated().verify_monthly_disposable_income_is_calculated()
            return self

        def navigate_to_retirement_tab(self):
            ProfileStage(self.config).click_select_retirement()
            BaseFactFindPage(self.config).click_save_button()
            RetirementStage(self.config).click_retirement_tab()
            return self

        def fill_state_pension_form(self):
            eligibility = RetirementStage.Eligibility(self.config)
            return RetirementStage(self.config).fill_in_form(
                get_common_data(self.config)["test_data"]["fact_find_retirement_state_pension_form"],
                eligibility).click(
                BaseFactFindPage.Locators.SAVE_BUTTON)

        def add_retirement_goals_growth_with_target(self):
            return self.add_retirement_contract(
                get_common_data(self.config)["test_data"][
                    "fact_find_retirement_goals_retirement_form - Growth with Target"])

        def add_retirement_goals_lump_sum(self):
            return self.add_retirement_contract(
                get_common_data(self.config)["test_data"]["fact_find_retirement_goals_retirement_form - Lump Sum"])

        def add_retirement_contract(self, data):
            goals = RetirementStage.Goals(self.config)
            return goals.click_add_button().fill_in_form(data, goals).click_save_button()

        def add_retirement_details(self):
            retirement = RetirementStage(self.config)
            retirement.click_goals_subtab()
            self.add_retirement_goals_growth_with_target()
            self.add_retirement_goals_lump_sum()
            retirement.click_eligibility_and_entitlement_subtab()
            retirement_eligibility = RetirementStage.Eligibility(self.config)
            retirement_eligibility.click_pension_scheme_radiobutton_yes()
            retirement_eligibility.click_member_radiobutton_yes()
            self.fill_state_pension_form()
            retirement.click_final_salary_subtab()
            retirement_final_salary = RetirementStage.FinalSalary(self.config)
            retirement_final_salary.click_existing_schemes_radiobutton_yes()
            retirement_final_salary.click_save_button()
            retirement.click_money_purchase_subtab()
            retirement_money_purchase = RetirementStage.MoneyPurchase(self.config)
            retirement_money_purchase.click_existing_schemes_radiobutton_yes()
            retirement_money_purchase.click_save_button()
            retirement.click_personal_pensions_subtab()
            retirement_personal_pensions = RetirementStage.PersonalPensions(self.config)
            retirement_personal_pensions.click_existing_schemes_radiobutton_yes()
            retirement_personal_pensions.click_save_button()
            retirement.click_annuities_subtab()
            retirement_annuities = RetirementStage.Annuities(self.config)
            retirement_annuities.click_existing_schemes_radiobutton_yes()
            retirement_annuities.click_save_button()
            retirement.click_next_steps_subtab()
            return self

        def verify_retirement_goals_added(self):
            data = RetirementStage.NextSteps(self.config).get_retirement_goals_str_list()
            assert utils.is_string_present(data, get_common_data(self.config)[
                "test_data"]["fact_find_retirement_goals_retirement_form - Growth with Target"]["GOAL_TYPE"]), \
                "Retirement Goals with Growth with Target wasn't saved successfully"
            assert utils.is_string_present(data, get_common_data(self.config)["test_data"][
                "fact_find_retirement_goals_retirement_form - Lump Sum"]["GOAL_TYPE"]), \
                "Retirement Goals with Lump Sum wasn't saved successfully"
            return self

        def navigate_to_estate_planning_tab(self):
            ProfileStage(self.config).click_select_estate_planning()
            BaseFactFindPage(self.config).click_save_button()
            EstatePlanningStage(self.config).click_estate_planning_tab()
            return self

        def fill_goals_or_needs(self):
            goals = EstatePlanningStage.Goals(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_estate_planning_goals_or_needs_form"]
            goals.fill_in_field(goals.Locators.__dict__.get("GOALS_OR_NEEDS"), data["GOALS_OR_NEEDS"])
            goals.click_save_button()
            return self

        def fill_current_position_form(self):
            current_position = EstatePlanningStage.CurrentPosition(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_estate_planning_current_position_form"]
            for i in data:
                current_position.fill_in_field(current_position.Locators.__dict__.get(i), data[i])
            current_position.click_save_button()
            return self

        def fill_next_steps(self):
            next_steps = EstatePlanningStage.NextSteps(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_estate_planning_next_steps_form"]
            next_steps.fill_in_field(next_steps.Locators.__dict__.get("NEXT_STEPS"), data["NEXT_STEPS"])
            next_steps.click_save_button()
            return self

        def add_estate_planning_details(self):
            estate_planning = EstatePlanningStage(self.config)
            estate_planning.click_goals_subtab()
            self.fill_goals_or_needs()
            estate_planning.click_current_position_subtab()
            self.fill_current_position_form()
            estate_planning.click_next_steps_subtab()
            self.fill_next_steps()
            return self

        def verify_estate_planning_forms(self):
            EstatePlanningStage(self.config).click_goals_subtab()
            assert EstatePlanningStage.Goals(self.config).get_goals_form_value() == \
                   get_common_data(self.config)["test_data"]["fact_find_estate_planning_goals_or_needs_form"][
                       "GOALS_OR_NEEDS"], \
                "Goals or Needs wasn't saved successfully"
            EstatePlanningStage(self.config).click_current_position_subtab()
            assert EstatePlanningStage.CurrentPosition(self.config).get_current_position_broad_content_value() == \
                   get_common_data(self.config)["test_data"]["fact_find_estate_planning_current_position_form"][
                       "BROAD_CONTENT"], "Broad Content wasn't saved successfully"
            EstatePlanningStage(self.config).click_next_steps_subtab()
            assert EstatePlanningStage.NextSteps(self.config).get_next_steps_value() == \
                   get_common_data(self.config)["test_data"]["fact_find_estate_planning_next_steps_form"][
                       "NEXT_STEPS"], "Next Steps wasn't saved successfully"

        def add_summary_details(self):
            factfind = BaseFactFindPage(self.config)
            factfind.click_summary_tab()
            summary = SummaryStage(self.config)
            summary.click_marketing_subtab()
            data = get_common_data(self.config)["test_data"]["fact_find_data"]
            summary.fill_in_consent_date_fields(data["CONSENT_DATE"])
            summary.click_save_button()
            return self

        def navigate_to_mortgage(self):
            factfind = BaseFactFindPage(self.config)
            factfind.click_profile_tab()
            profile = ProfileStage(self.config)
            profile.click_select_mortgage()
            profile.click_save_button()
            factfind.click_mortgage_tab()
            return self

        def fill_existing_property_details_form(self):
            property = MortgageStage.PropertyDetails(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_add_existing_property_details"]
            for i in data:
                property.fill_in_field(property.Locators.__dict__.get(i), data[i])
            MortgageStage(self.config).click_form_save_button()
            return self

        def fill_existing_mortgage_form(self):
            mortgage = MortgageStage.ExistingProvision(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_add_existing_mortgage_buy_to_let_regulated"]
            for i in data:
                mortgage.fill_in_field(mortgage.Locators.__dict__.get(i), data[i])
            MortgageStage(self.config).click_form_save_button()
            return self

        def fill_mortgage_requirements_form(self):
            requirement = MortgageStage.Requirements(self.config)
            data = get_common_data(self.config)["test_data"]["fact_find_add_mortgage_requirements_buy_to_let_regulated"]
            for i in data:
                requirement.fill_in_field(requirement.Locators.__dict__.get(i), data[i])
            MortgageStage(self.config).click_form_save_button()
            return self

        def add_mortgage_details(self):
            mortgage = MortgageStage(self.config)
            mortgage.click_existing_provision_subtab()
            mortgage_existingprovision = MortgageStage.ExistingProvision(self.config)
            mortgage_existingprovision.click_yes_radiobutton()
            mortgage_existingprovision.click_add_button()
            self.fill_existing_mortgage_form()
            mortgage.click_save_button()
            mortgage.click_property_details_subtab()
            mortgage_propertydetails = MortgageStage.PropertyDetails(self.config)
            mortgage_propertydetails.click_add_button()
            self.fill_existing_property_details_form()
            mortgage.click_requirements_subtab()
            mortgage_requirements = MortgageStage.Requirements(self.config)
            mortgage_requirements.click_add_button()
            self.fill_mortgage_requirements_form()
            mortgage.click_preferences_and_risk_subtab()
            mortgage_preferencerisk = MortgageStage.PreferencesAndRisk(self.config)
            mortgage_preferencerisk.click_radiobutton()
            mortgage.click_save_button()
            return self.journey

        def finish(self):
            return self.journey

    class _LinkedDocuments:

        def __init__(self, client_id, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = LinkedDocumentsDialog(client_id, parent_page)

        def open_linked_documents(self):
            self.dialog.click_view_button()
            return self.journey

    class _ViewPDFs:
        def __init__(self, client_id, factfind_ref, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.dialog = ViewPDFSDialog(client_id, factfind_ref, parent_page)

        def add_document(self):
            self.dialog.click_add_document_button()
            self.dialog.wait_until_please_wait_spinner_present()
            return self

        def close_dialog(self):
            self.dialog.click_close_button()
            return self.journey

        def download_the_pdf(self):
            self.dialog.click_open_first_document()
            time.sleep(1)
            return self

    class _VerifyDocuments:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey

        def verify_saved_documents(self):
            ClientDocumentsPage(self.config).verify_document_exists()
            return self.journey

    class _VerifyOpportunity:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.opportunities = OpportunitiesPage(self.config)
            assert self.opportunities.is_title_matches(), "Title does not match the opportunities section"

        def verify_saved_opportunity(self):
            self.opportunities.verify_opportunity_exists()
            return self.journey
