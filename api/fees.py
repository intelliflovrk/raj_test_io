import json
import utils


def create_fee_for_client(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "create_fee"))
    result = config.post(f"/v2/clients/{client_id}/fees", "charging", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()
