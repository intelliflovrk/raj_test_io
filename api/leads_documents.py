def delete_leads_document(config, lead_id, document_id):
    result = config.delete(f"/v2/leads/{lead_id}/documents/{document_id}", "storage")
    assert result.status_code == 204, \
        f"Expected response code is 204. Actual response code is {result.status_code} {result.text}"


def get_leads_documents(config, lead_id):
    result = config.get(f"/v2/leads/{lead_id}/documents", "storage")
    assert result.status_code == 200, \
        f"Expected response code is 200. Actual response code is {result.status_code} {result.text}"
    return result.json()
