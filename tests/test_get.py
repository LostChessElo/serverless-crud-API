import json
from get_handler import get_handler

def test_empty_table_returns_empty_list(mock_table):
    response = get_handler()
    assert response.get("statusCode") == 200
    assert response.get("headers").get("Content-Type") == "application/json"
    assert response.get("body") == "[]"

def test_get_returns_content_of_table(mock_table):
    mock_table.put_item(
        Item={"id": "usr_123", "name": "test note", "description": "note to test"}
    )
    
    response = get_handler()
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert isinstance(body, list)
    assert isinstance(body[0], dict)
    assert body[0].get("name") == "test note"
    assert body[0].get("description") == "note to test"