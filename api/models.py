
def get_portfolio_models(config):
    config.get_access_token_for_resource_owner_flow()
    result = config.get(f"/v2/models", "portfolio")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    config.access_token = None
    return result.json()


def deactivate_portfolio_model(config, model_id):
    config.get_access_token_for_resource_owner_flow()
    result = config.post(f"/v2/models/{model_id}/active?isActive=false", "portfolio")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    config.access_token = None

