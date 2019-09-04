import json
import utils


def create_valuation(config, client_id, plan_id, valuation="40000.0000"):
    data = json.loads(utils.get_api_test_data(config, "create_valuation"))
    data["value"]["amount"] = valuation
    result = config.post(f"/v2/clients/{client_id}/plans/{plan_id}/valuations", "portfolio",
                         data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()
