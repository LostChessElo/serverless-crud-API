import json
from db import table
from response import ok, error
from botocore.exceptions import ClientError

from typing import Any
from aws_lambda_typing.events import APIGatewayProxyEventV1
from aws_lambda_typing.context import Context


def post_handler(event: APIGatewayProxyEventV1, context: Context) -> dict[str, Any]:
    try:
        raw_data = event.get("body")
        if not raw_data:
            return error(400, "Bad request.")

        body: Any = json.loads(raw_data)
        err = _validate_rq_body(body)
        if err:
            return error(400, err)

        note_id = context.aws_request_id
        table.put_item(
            Item={
                "id": note_id,
                "name": body["name"],
                "description": body["description"],
            }
        )

        return ok({"message": "Note added successfully."}, 200)

    except json.JSONDecodeError:
        return error(400, "Bad request.")
    except ClientError as e:
        return error(500, e.response["Error"]["Message"])


def _validate_rq_body(body: Any) -> None | str:
    if not isinstance(body, dict):
        return "Bad request."
    if "name" not in body or not body["name"]:
        return "Bad request."
    if "description" not in body:
        return "Bad request."
    return None
