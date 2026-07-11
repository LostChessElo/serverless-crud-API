import json 
from post_handler import post_handler

class Context:
    def __init__(self):
        self.aws_request_id = "123ABC"

    def get_id(self):
        return self.aws_request_id


def test_vaid_rq_body_returns_200(mock_table):
    context = Context()
    event = {
        "body": '{"name": "test note", "description": "Note to test"}'
    }

    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert body.get("message") != None
    assert body.get("message") == "Note added successfully."

def test_note_already_exists_returns_200(mock_table):
    mock_table.put_item(
        Item={
            "id": "123ABC",
            "name": "test note",
            "description": "Note to test"
        }
    )
    context = Context()
    event = {
        "body": '{"name": "test note", "description": "Note to test"}'
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 200
    assert body.get("message") != None
    assert body.get("message") == "Note added successfully."

def test_empty_name_returns_400(mock_table):
    context = Context()
    event = {
        "body": '{"name": "", "description": "Note to test"}'
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."

def test_malformed_rqq_body_returns_400(mock_table):
    context = Context()
    event = {
        "body": '[]'
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."

def test_no_description_returns_400(mock_table):
    context = Context()
    event = {
        "body": '{"name": "123"}'
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."

def test_no_name_returns_400(mock_table):
    context = Context()
    event = {
        "body": '{ "description": "Note to test"}'
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."

def test_json_load_error_caught(mock_table):
    context = Context()
    event = {
        "body": "[]"
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."

def test_reqquest_not_json_returns_400(mock_table):
    context = Context()
    event = {
        "body": 'test'
    }
    response = post_handler(event, context)
    body = json.loads(response.get("body"))
    assert response.get("statusCode") == 400
    assert body.get("message") != None
    assert body.get("message") == "Bad request."