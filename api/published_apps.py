

def install_app(config, app_id):
    config.get_access_token_for_resource_owner_flow()
    result = config.post(f"/v2/published_apps/{app_id}/installation", "appd")
    assert result.status_code == 201, \
        f"Expected response code is 201. Actual response code is {result.status_code} {result.text}"


def uninstall_app(config, app_id):
    config.get_access_token_for_resource_owner_flow()
    result = config.delete(f"/v2/published_apps/{app_id}/installation", "appd")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"
