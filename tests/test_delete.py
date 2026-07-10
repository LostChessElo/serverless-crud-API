import json
from delete_handler import delete_handler 

def test_delete_note_returns_ok(mock_table):
    mock_table.put_item(
        Item={"id": "usr_123", "name": "test note", "description": "note to test"}
    )

    event = {
        "pathParameters": {
            "id": "usr_123"
        }
    }

    response = delete_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert isinstance(body, dict)
    assert body.get("message") != None
    assert body.get("message") == "Note deleted successfully."

def test_delete_note_on_non_existent_id_returns_404(mock_table):
    mock_table.put_item(
        Item={"id": "usr_123", "name": "test note", "description": "note to test"}
    )

    event = {
        "pathParameters": {
            "id": "123abc"
        }
    }

    response = delete_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 404
    assert body.get("message") != None
    assert body.get("message") == "Note not found."

def test_no_id_returns_400(mock_table):
    mock_table.put_item(
        Item={"id": "usr_123", "name": "test note", "description": "note to test"}
    )

    event = {
        "pathParameters": {
            
        }
    }

    response = delete_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."
