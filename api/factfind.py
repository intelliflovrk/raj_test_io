import utils
import json
from datetime import datetime, timedelta


def create_client_goal(config, client_id):
    data = json.loads(utils.get_api_test_data(config, "create_goal"))
    data["startDate"] = datetime.now().strftime("%Y-%m-%d")
    target_date = datetime.now() + timedelta(days=3600)
    data["targetDate"] = target_date.strftime("%Y-%m-%d")
    result = config.post(f"/v1/clients/{client_id}/goals", "factfind", data=json.dumps(data))
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"
    return result.json()


def delete_client_goal(config, client_id, goal_id):
    result = config.delete(f"/v1/clients/{client_id}/goals/{goal_id}", "factfind")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"