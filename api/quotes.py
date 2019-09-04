import json
import utils


def create_quote(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "create_quote"))
    result = config.post(f"/v2/clients/{client_id}/quotes/", "quotation", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def set_quote_status(config, client_id, quote_id, status):
    result = config.post(f"/v2/clients/{client_id}/quotes/{quote_id}/status/{status}", "quotation")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"


def create_quote_result(config, client_id, quote_id, *client_id_second_life):
    data = json.loads(utils.get_api_test_data(config, "create_quote_result"))
    data["applicants"][0]["id"] = client_id
    if client_id_second_life:
        data["applicants"].append({"id": f"{client_id_second_life[0]}"})
    result = config.post(f"/v2/clients/{client_id}/quotes/{quote_id}/results", "quotation", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def add_second_life_to_quote(config, client_id_second_life, quote_id):
    result = config.post(f"/v2/clients/{client_id_second_life}/quotes/{quote_id}", "quotation")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return config
