from datetime import date
import json
import utils


def create_withdrawal(config, client_id, plan_id):
    data = json.loads(utils.get_api_test_data(config, "create_withdrawal"))
    data["startsOn"] = date.today().strftime("%Y-%m-%d")
    result = config.post(f"/v2/clients/{client_id}/plans/{plan_id}/withdrawals", "portfolio",
                         data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_withdrawal(config, client_id, plan_id, withdrawal_id):
    result = config.delete(f"/v2/clients/{client_id}/plans/{plan_id}/withdrawals/{withdrawal_id}", "portfolio")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}."
