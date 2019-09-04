import utils
import json
import fakedata


def create_model_portfolio(config):
    data = json.loads(utils.get_api_test_data(config, "create_basic_imps_model"))
    data["code"] = data["code"] + fakedata.rand_text()
    data["name"] = "Automation Rebalance Test iMPS Model " + fakedata.rand_text()
    config.access_token = config.get_app_tcc_token("imps_app")
    app_id = utils.get_app_by_type(config, "imps_app")["app_id"]
    result = config.post(f"/v2/apps/{app_id}/models", "imps", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    config.access_token = None
    return result.json()


def accept_model_portfolio(config, model_id):
    config.get_access_token_for_resource_owner_flow()
    tenant_id = utils.get_automation_tenant_id(config)
    result = config.post(f"/v2/installed_apps/models/{model_id}/accept?tenantId={tenant_id}", "imps")
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    config.access_token = None
