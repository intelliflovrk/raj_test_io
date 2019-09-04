from datetime import date
import json
import utils


def create_fund_holding(config, client_id, plan_id):
    data = json.loads(utils.get_api_test_data(config, "create_fund"))
    data["units"]["numberUpdatedOn"] = date.today().strftime("%Y-%m-%d")
    data["units"]["priceUpdatedOn"] = date.today().strftime("%Y-%m-%d")
    result = config.post(f"/v2/clients/{client_id}/plans/{plan_id}/holdings", "portfolio",
                         data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


# <editor-fold desc="fund proposal"

def delete_fundproposal_for_plan(config, client_id, plan_id):
    result = config.delete(f"/v2/clients/{client_id}/plans/{plan_id}/fundproposal", "portfolio",)
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def add_model_to_plan_fundproposal(config, client_id, plan_id, model_id):
    data = json.loads(utils.get_api_test_data(config, "add_imps_model_to_fund_proposal"))
    data["model"]["id"] = model_id
    result = config.put(f"/v2/clients/{client_id}/plans/{plan_id}/fundproposal", "portfolio", data=json.dumps(data))
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()
# </editor-fold>
