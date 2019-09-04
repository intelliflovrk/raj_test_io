import json
import utils


def create_task(config, client_id):
    config.get_access_token_using_internal_credentials()
    data = json.loads(utils.get_api_test_data(config, "create_task"))
    data["relatedPartyId"] = client_id
    result = config.post(f"/v1/tasks", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()
