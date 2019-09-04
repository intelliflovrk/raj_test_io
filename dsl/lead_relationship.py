import utils
from dsl.create_lead import CreateLead
from dsl.search import SearchLead
from ioffice.clients.add_relationship_wizard import AddRelationshipWizard
from ioffice.leads.lead_details_page import LeadDetailsPage
from ioffice.leads.relationships import ViewRelationshipsPage


class AddLeadRelationship(SearchLead, CreateLead):

    def navigate_to_relationships(self):
        LeadDetailsPage(self.config)\
            .click_details()\
            .click_relationships_tab()
        return self

    def using_add_relationship_wizard(self):
        lead_details_page = LeadDetailsPage(self.config)
        lead_details_page.lead_actions_menu() \
            .hover_over_lead_actions() \
            .click_add_relationship()
        return AddLeadRelationship._AddRelationship(lead_details_page, self)

    def verify_relationship_added(self):
        relationship_id = ViewRelationshipsPage(self.config).get_first_relationship_id()
        utils.add_temp_data(self.config, "lead_relationship", {"id": relationship_id})
        data = utils.get_common_data(self.config)["clients"]["default"]
        assert data["firstname"] + " " + data["lastname"] == ViewRelationshipsPage(
            self.config).get_first_relationship_name(), "Incorrect relationship name"
        assert utils.get_common_data(self.config)["test_data"]["add_relationship_data"]["spouse"] == \
            ViewRelationshipsPage(self.config).get_first_relationship(), "Incorrect relationship"

    class _AddRelationship:
        def __init__(self, parent_page, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddRelationshipWizard(parent_page)

        def add_relationship_to_lead(self):
            client = utils.get_common_data(self.config)["clients"]["default"]
            self.wizard.select_type_stage() \
                .select_radio_button_person()
            self.wizard.search_contact_stage() \
                .goto_stage() \
                .fill_in_firstname(client["firstname"]) \
                .fill_in_lastname(client["lastname"])
            self.wizard.select_contact_stage() \
                .goto_stage() \
                .select_contact_radio_button()
            self.wizard.finish_stage() \
                .goto_stage() \
                .select_relationship(utils.get_common_data(self.config)["test_data"]["add_relationship_data"]["spouse"])
            self.wizard.finish_stage() \
                .goto_stage() \
                .click_complete_button()
            return self.journey
