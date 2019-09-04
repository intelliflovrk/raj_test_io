import utils
from dsl.create_client import CreateClient, get_common_data
from ioffice.clients.add_relationship_wizard import AddRelationshipWizard
from ioffice.clients.client_dashboard import ClientDashboardPage
from ioffice.clients.details.relationships import ClientRelationshipsPage


class AddRelationship(CreateClient):

    def using_add_relationship_wizard(self):
        ClientDashboardPage(self.config)\
            .client_actions_menu() \
            .hover_over_client_actions() \
            .add_relationship()
        self.wizard = AddRelationship._RelationshipWizard(self)
        return self.wizard

    def verify_corporate_client_relationship(self):
        relationship_id = ClientRelationshipsPage(self.config).get_relationship_id()
        utils.add_temp_data(self.config, "client_relationship", {"id": relationship_id})
        client = utils.get_common_data(self.config)["clients"]["default"]
        assert ClientRelationshipsPage(self.config).get_first_employee_name() == client["firstname"] + " " + client["lastname"], \
            "Incorrect Employee Name"
        assert ClientRelationshipsPage(self.config).get_first_employee_relationship() == utils.get_common_data(
            self.config)["test_data"]["add_relationship_data"]["employee"], "Incorrect Relationship"
        return self

    class _RelationshipWizard:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.wizard = AddRelationshipWizard(self.config)

        def add_employee_relationship(self):
            client = utils.get_common_data(self.config)["clients"]["default"]
            self.select_person_contact_type()\
                .fill_in_client_name(client["firstname"], client["lastname"])\
                .select_client()\
                .select_relationship()
            return self

        def select_person_contact_type(self):
            self.wizard.select_type_stage()\
                .select_radio_button_person()
            return self

        def fill_in_client_name(self, first_name, last_name):
            self.wizard.search_contact_stage()\
                .goto_stage()\
                .fill_in_firstname(first_name)\
                .fill_in_lastname(last_name)
            return self

        def select_client(self):
            self.wizard.select_contact_stage()\
                .goto_stage()\
                .select_contact_radio_button()
            return self

        def select_relationship(self):
            self.wizard.finish_stage() \
                .goto_stage()\
                .select_relationship(get_common_data(self.config)["test_data"]["add_relationship_data"]["employee"])
            return self

        def finish(self):
            self.wizard.finish_stage()\
                .goto_stage()\
                .click_complete_button()
            return self.journey
