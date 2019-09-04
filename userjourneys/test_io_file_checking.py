import pytest
from dsl.file_checking import FileChecking

pytestmark = [pytest.mark.file_checking, pytest.mark.io_all]


@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='fails on tst')
@pytest.mark.post_submission
@pytest.mark.usefixtures("api_delete_plan")
@pytest.mark.usefixtures("api_change_plan_status_to_submitted_to_provider")
@pytest.mark.usefixtures("api_create_mortgage_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_post_search_checks(config):
    """ Test Description: Adding an mortgage plan and verify post-search checks. """
    test = (FileChecking(config)
            .navigate_to_post_search()
                .search_and_open_client()
                .wait_until_post_search_results_appear()
            .verify_plan_present_in_search_results()
            )


@pytest.mark.skip(reason="Blocked because of IP-49056")
@pytest.mark.pre_submission
@pytest.mark.usefixtures("api_change_plan_status_to_compliance_sign_off")
@pytest.mark.usefixtures("api_create_mortgage_plan")
@pytest.mark.usefixtures("api_search_default_client_and_save_details")
@pytest.mark.usefixtures("ui_login_logout")
def test_pre_search_checks(config):
    """ Test Description: Adding an mortgage plan and verify pre-search checks. """
    test = (FileChecking(config)
            .navigate_to_pre_search()
                .search_and_open_client()
            .wait_until_pre_search_results_appear()
            .verify_plan_present_in_search_results()
            )
