import json
import utils


def create_relationships_for_client(config, client_id_first_life, client_id_second_life, relationship_type=None):
    data = json.loads(utils.get_api_test_data(config, "create_relationships"))
    data["subject"]["id"] = client_id_first_life
    data["relation"]["id"] = client_id_second_life
    if relationship_type:
        data["relationshipType"]["name"] = relationship_type
    result = config.post(f"/v2/clients/{client_id_first_life}/relationships", "crm", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_relationship_for_client(config, client_id, relationship_id):
    result = config.delete(f"/v2/clients/{client_id}/relationships/{relationship_id}", "crm")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def delete_relationship_for_lead(config, lead_id, relationship_id):
    result = config.delete(f"/v2/leads/{lead_id}/relationships/{relationship_id}", "crm")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"