import utils
import json
import fakedata


def create_client(config):
    data = json.loads(utils.get_api_test_data(config, "create_client"))
    data["person"]["firstName"] = data["person"]["firstName"] + fakedata.rand_text()
    data["person"]["lastName"] = data["person"]["lastName"] + fakedata.rand_text()
    result = config.post("/v2/clients", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def add_address_for_client(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "create_address"))
    result = config.post(f"/v2/clients/{client_id}/addresses", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def get_addresses_for_client(config, client_id):
    result = config.get(f"/v2/clients/{client_id}/addresses", "crm",)
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def get_employment_for_client(config, client_id):
    result = config.get(f"/v2/clients/{client_id}/employments", "factfind",)
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_address_for_client(config, client_id, address_id):
    result = config.delete(f"/v2/clients/{client_id}/addresses/{address_id}", "crm",)
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def delete_employment_for_client(config, client_id, employment_id):
    result = config.delete(f"/v2/clients/{client_id}/employments/{employment_id}", "factfind",)
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def create_corporate_client(config):
    data = json.loads(utils.get_api_test_data(config, "create_corporate_client"))
    data["corporate"]["name"] = data["corporate"]["name"] + fakedata.rand_text()
    result = config.post("/v2/clients", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def update_cff_client_personal_data(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "reset_cff_client_data"))
    result = config.put(f"/v2/clients/{client_id}", "crm", data=json.dumps(data))
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def add_personal_details_to_cff_client(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "cff_about_you_segment_client_data"))
    result = config.put(f"/v2/clients/{client_id}", "crm", data=json.dumps(data))
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def add_personal_details_to_cff_client(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "cff_about_you_segment_client_data"))
    result = config.put(f"/v2/clients/{client_id}", "crm", data=json.dumps(data))
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def search_client(config, last_name):
    config.get_access_token_for_resource_owner_flow()
    data = json.loads(utils.get_api_test_data(config, "search_client"))
    data["filters"][0]["value"] = last_name
    result = config.post("/v1/clients/search", "crm", data=json.dumps(data))
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


# <editor-fold desc="client contact details">
def add_contact_for_client(config, client_id, contact_type):
    data = json.loads(utils.get_api_test_data(config, "create_client_contact"))
    data["type"] = contact_type
    result = config.post(f"/v2/clients/{client_id}/contactdetails", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def get_contacts_for_client(config, client_id):
    result = config.get(f"/v2/clients/{client_id}/contactdetails", "crm",)
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_contact_for_client(config, client_id, contact_id):
    result = config.delete(f"/v2/clients/{client_id}/contactdetails/{contact_id}", "crm",)
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"
# </editor-fold>
