import pytest
from dsl.income_administration import IncomeAdministration

pytestmark = [pytest.mark.io_all, pytest.mark.payment, pytest.mark.first]


@pytest.mark.skip(reason="PRD Defect IP-55473")
@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='fails on tst')
@pytest.mark.usefixtures("ui_login_logout")
def test_payment_run(config):
    """ Test Description: Start payment run and verify data in payment history. """
    test = (IncomeAdministration(config)
            .navigate_to_payment_run()
                .start_payment_run()
            .navigate_to_payment_history()
            .verify_payment_run_presence_in_payment_history()
            )


@pytest.mark.skip(reason="PRD Defect IP-55473")
@pytest.mark.skipif('tst-02' == pytest.config.option.env, reason='fails on tst')
@pytest.mark.usefixtures("ui_login_logout")
def test_month_end_run(config):
    """ Test Description: Start month end and verify data in period end history. """
    test = (IncomeAdministration(config)
            .navigate_to_payment_run()
                .run_month_end()
            .navigate_to_period_end_history()
            .verify_month_end_presence_in_period_end_history()
            )
