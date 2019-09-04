import json
import utils


def get_dependants(config, client_id):
    result = config.get(f"/v2/clients/{client_id}/dependants", "factfind")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_dependant(config, client_id, dependant_id):
    result = config.delete(f"/v2/clients/{client_id}/dependants/{dependant_id}", "factfind")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def add_dependant(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "add_dependant"))
    result = config.post(f"/v2/clients/{client_id}/dependants", "factfind", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()