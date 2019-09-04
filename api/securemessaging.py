import utils
import json
import fakedata


def create_secure_message(config):
    config.get_access_token_for_resource_owner_flow()
    data = json.loads(utils.get_api_test_data(config, "create_secure_message"))
    data["subject"] = fakedata.rand_text(5)
    result = config.post("/v1/messages", "securemessaging", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def send_secure_message(config, message_id):
    config.get_access_token_for_resource_owner_flow()
    result = config.post(f"/v1/messages/{message_id}/sendtoadviser", "securemessaging")
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
