import json
from db import table
from response import ok, error
from botocore.exceptions import ClientError

from typing import Any
from aws_lambda_typing.events import APIGatewayProxyEventV1


def patch_handler(event: APIGatewayProxyEventV1) -> dict[str, Any]:
    try:
        params = event.get("pathParameters") or {}
        note_id = params.get("id")

        if not note_id:
            return error(400, "Bad request.")

        # load old note for fallback
        old_note = table.get_item(Key={"id": note_id}).get("Item")

        if not old_note:
            return error(404, "Note not found.")

        raw_data = event.get("body") or "{}"
        # empty request body means no changes made return 200 ok
        body: Any = json.loads(raw_data)
        err: str | None = _validate_rq_body(body)
        if err:
            return error(400, err)
        if not body:
            return ok(old_note, 200)

        name: Any = (
            body.get("name") if body.get("name") is not None else old_note["name"]
        )
        description: Any = (
            body.get("description")
            if body.get("description") is not None
            else old_note["description"]
        )

        response = table.update_item(
            Key={"id": note_id},
            UpdateExpression="SET #name = :name_val, #description = :description_val",
            ExpressionAttributeNames={"#name": "name", "#description": "description"},
            ExpressionAttributeValues={
                ":name_val": name,
                ":description_val": description,
            },
            ReturnValues="ALL_NEW",
        )

        return ok(response["Attributes"], 200)
    except json.JSONDecodeError:
        return error(400, "Bad request.")
    except ClientError as e:
        return error(500, e.response["Error"]["Message"])


def _validate_rq_body(body: Any) -> None | str:
    if not isinstance(body, dict):
        return "Bad request."
    return None
