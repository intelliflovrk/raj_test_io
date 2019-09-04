from ioffice.clients.base import BaseClientPage
from ioffice.clients.add_opportunity_dialog import AddOpportunityDialog
from ioffice.clients.opportunities.base_opportunity import OpportunityBasePage
from ioffice.clients.opportunities.opportunities import OpportunitiesPage
from ioffice.clients.opportunities.delete_opportunity_dialog import DeleteOpportunityDialog
import utils


class ClientOpportunities:
    def __init__(self, config):
        self.config = config

    def add_opportunity(self):
        BaseClientPage(self.config)\
            .client_actions_menu()\
            .hover_over_client_actions()\
            .click_add_opportunity()
        AddOpportunityDialog(BaseClientPage(self.config))\
            .select_first_campaign_type()\
            .wait_until_please_wait_spinner_present()\
            .click_save()\
            .close_dialog()
        ClientOpportunities._ClientOpportunity(self)\
            .save_opportunity_ref().save_opportunity_id()
        return ClientOpportunities._ClientOpportunity(self)

    def navigate_to_opportunities(self):
        BaseClientPage(self.config)\
            .level3_menu()\
            .click_opportunities()
        return ClientOpportunities._ClientOpportunities(self)

    class _ClientOpportunity:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey

        def save_opportunity_ref(self):
            opportunity_ref = OpportunityBasePage(self.config)\
                .get_opportunity_ref()
            utils.add_temp_data(self.config, "opportunity", {"reference": opportunity_ref})
            return self

        def save_opportunity_id(self):
            opportunity_id = OpportunityBasePage(self.config)\
                .get_opportunity_id()
            utils.update_temp_data(self.config, "opportunity", 0, "id", opportunity_id)
            return self

        def delete_opportunity(self):
            OpportunityBasePage(self.config)\
                .hover_over_opportunity_actions()\
                .click_delete_opportunity()
            DeleteOpportunityDialog(OpportunityBasePage(self.config))\
                .click_yes()\
                .wait_until_please_wait_spinner_present()\
                .close_dialog()
            return ClientOpportunities._ClientOpportunities(self)

    class _ClientOpportunities:
        def __init__(self, journey):
            self.config = journey.config
            self.journey = journey
            self.page = OpportunitiesPage(self.config)

        def open_opportunity(self):
            self.page.click_open(utils.get_temp_data(self.config, "opportunity")["id"])
            return ClientOpportunities._ClientOpportunity(self)
