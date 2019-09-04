import json
import fakedata
import utils


def create_lead(config):
    data = json.loads(utils.get_api_test_data(config, "create_lead"))
    data["person"]["firstName"] = data["person"]["firstName"] + fakedata.rand_text()
    data["person"]["lastName"] = data["person"]["lastName"] + fakedata.rand_text()
    result = config.post("/v2/leads", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_lead(config, lead_id):
    result = config.delete(f"/v2/leads/{lead_id}", "crm")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def add_address_for_lead(config, lead_id):
    data = json.loads(utils.get_api_test_data(config, "create_address"))
    result = config.post(f"/v2/leads/{lead_id}/addresses", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()