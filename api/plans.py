import json

import utils


def change_plan_status_to(config, client_id, plan_id, status):
    data = json.loads(utils.get_api_test_data(config, "change_plan_status"))
    data["status"] = status
    result = config.post(f"/v2/clients/{client_id}/plans/{plan_id}/statuses", "portfolio",
                         data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def create_plan(config, client_id, plan_type, is_pre_existing=False, plan_details={}):
    data = json.loads(utils.get_api_test_data(config, "create_plan"))
    if is_pre_existing:
        data["Lifecycle"]["id"] = data["Lifecycle"]["id"]["is_pre_existing"]
    else:
        data["Lifecycle"]["id"] = data["Lifecycle"]["id"][plan_type]
    data["planType"]["name"] = data["planType"]["name"][plan_type]
    data["owners"][0]["id"] = client_id
    data.update(plan_details)
    result = config.post(f"/v2/clients/{client_id}/plans/", "portfolio", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def get_plans_for_a_client(config, client_id):
    result = config.get(f"/v2/clients/{client_id}/plans/", "portfolio")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()
