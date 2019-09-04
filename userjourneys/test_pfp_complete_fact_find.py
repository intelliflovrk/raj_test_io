import pytest
from dsl.complete_pfp_factfind import FactFind

pytestmark = [pytest.mark.pfp]


@pytest.mark.usefixtures("ui_pfp_login")
@pytest.mark.usefixtures("api_delete_client_dependants")
@pytest.mark.usefixtures("ui_logout")
@pytest.mark.usefixtures("api_update_cff_client_personal_details")
def test_complete_basic_details(config):
    """ Test Description: Complete About You and Your Family segments with basic details and verify data sync in iO """
    test = (FactFind(config)
            .using_your_profile()
                .start_fact_find_completion()
                .using_you_and_your_family()
                    .using_about_you_wizard()
                        .add_basic_personal_details()
                    .using_your_family()
                        .add_dependant()
            .logout_pfp()
            .login_io()
            .search_open_gff_client()
            .open_client_fact_find()
                .navigate_to_personal_tab()
                    .verify_personal_client_data_syncronized()
                .navigate_to_dependants_tab()
                    .verify_dependants_data_syncronized()
            )


@pytest.mark.usefixtures("ui_pfp_logout")
@pytest.mark.usefixtures("api_update_cff_client_personal_details")
@pytest.mark.usefixtures("api_fill_in_about_you_segment_with_basic_details")
def test_update_client_personal_details_in_io(config):
    """ Test Description: Update client personal details in iO and verify data sync in PFP """
    test = (FactFind(config)
            .login_io()
            .search_open_gff_client()
            .open_client_fact_find()
                .navigate_to_personal_tab()
                    .fill_in_middle_name()
                    .update_marital_status()
            .logout_io()
            .login_pfp()
            .using_your_profile()
                .start_fact_find_completion()
                .using_you_and_your_family()
                    .using_about_you_wizard()
                        .verify_personal_data_was_updated()
            )


@pytest.mark.usefixtures("api_delete_client_employment")
@pytest.mark.usefixtures("ui_logout")
@pytest.mark.usefixtures("api_update_cff_client_personal_details")
@pytest.mark.usefixtures("api_fill_in_about_you_segment_with_basic_details")
@pytest.mark.usefixtures("ui_pfp_login")
def test_complete_data_segment_employment(config):
    """ Test Description: Add an employment in 'You and Your Family' and verify it on IO"""
    test = (FactFind(config)
            .navigate_to_you_and_your_family()
            .using_employment_segment()
                .add_current_employment_record()
                .save_and_close()
            .logout_pfp()
            .login_io()
            .search_open_gff_client()
            .open_client_fact_find()
            .navigate_to_employment_tab()
                .verify_employment_data_synchronized()
            )

