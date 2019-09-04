
def delete_tag_for_client(config, client_id, tag_name):
    result = config.delete(f"/v2/clients/{client_id}/tags/{tag_name}", "crm")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"
