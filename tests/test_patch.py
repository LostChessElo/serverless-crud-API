import json
from patch_handler import patch_handler


def test_update_note_returns_200(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {
        "pathParameters": {"id": "test123"},
        "body": '{"name": "test update", "description": "testing testing 123"}',
    }

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert body.get("name") == "test update"
    assert body.get("description") == "testing testing 123"


def test_empty_rq_body_returns_200_with_old_note(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {"pathParameters": {"id": "test123"}, "body": "{}"}

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert body.get("name") == "test note"
    assert body.get("description") == "Note to test"


def test_name_only_update_returns_200(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {"pathParameters": {"id": "test123"}, "body": '{"name": "test update"}'}

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert body.get("name") == "test update"
    assert body.get("description") == "Note to test"


def test_description_only_update_returns_200(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {
        "pathParameters": {"id": "test123"},
        "body": '{"description": "testing testing 123"}',
    }

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert body.get("name") == "test note"
    assert body.get("description") == "testing testing 123"


def test_no_id_returns_400(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {
        "pathParameters": {"id": ""},
        "body": '{"description": "testing testing 123"}',
    }

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") == "Bad request."


def test_wrong_note_id_returns_404(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {
        "pathParameters": {"id": "test12"},
        "body": '{"description": "testing testing 123"}',
    }

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 404
    assert body.get("message") == "Note not found."


def test_malformed_rq_body_returns_400(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {"pathParameters": {"id": "test123"}, "body": "TEST"}

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") == "Bad request."


def test_invalid_decodertype_returns_400(mock_table):
    mock_table.put_item(
        Item={"id": "test123", "name": "test note", "description": "Note to test"}
    )

    event = {"pathParameters": {"id": "test123"}, "body": "[]"}

    response = patch_handler(event)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") == "Bad request."
