import json
import utils
from fakedata import rand_text


def delete_workflow(config, workflow_id):
    config.get_access_token_using_internal_credentials()
    result = config.delete(f"/v1/templates/{workflow_id}", "workflow")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def change_workflow_status_to(config, workflow_id, status):
    config.get_access_token_using_internal_credentials()
    data = json.loads(utils.get_api_test_data(config, "change_workflow_status"))
    data["status"] = status
    result = config.patch(f"/v1/templates/{workflow_id}", "workflow", data=json.dumps(data))
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"


def create_workflow_category(config):
    config.get_access_token_using_internal_credentials()
    data = json.loads(utils.get_api_test_data(config, "create_workflow_category"))
    data["name"] = data["name"] + rand_text()
    result = config.post(f"/v1/templatecategories", "workflow", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_category(config, category_id):
    config.get_access_token_using_internal_credentials()
    result = config.delete(f"/v1/templatecategories/{category_id}", "workflow")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"

