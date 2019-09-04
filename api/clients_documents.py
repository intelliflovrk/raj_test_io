import json
import requests
import utils


def create_client_document(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "create_document"))
    result = config.post(f"/v2/clients/{client_id}/documents", "storage", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    config.document_location = result.headers["x-iflo-object-location"]
    return result.json()


def create_client_quote_document(config, client_id, quote_id):
    data = json.loads(utils.get_api_test_data(config, "create_quote_document"))
    data["linked_entities"][0]["id"] = quote_id
    result = config.post(f"/v2/clients/{client_id}/documents", "storage", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    config.document_location = result.headers["x-iflo-object-location"]


def create_client_quote_result_document(config, client_id, quote_result_id):
    data = json.loads(utils.get_api_test_data(config, "create_quote_result_document"))
    data["linked_entities"][0]["id"] = quote_result_id
    result = config.post(f"/v2/clients/{client_id}/documents", "storage", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    config.document_location = result.headers["x-iflo-object-location"]


def upload_client_document(location, file):
    result = requests.put(location, headers={'Content-Type': 'application/octet-stream'}, files={'file': file})
    assert result.status_code in (200, 204), \
        f"Expected response code is 200 or 204. Actual response code is {result.status_code} {result.text}"


def delete_client_document(config, client_id, document_id):
    result = config.delete(f"/v2/clients/{client_id}/documents/{document_id}", "storage")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def get_client_documents(config, client_id):
    result = config.get(f"/v2/clients/{client_id}/documents", "storage")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()
