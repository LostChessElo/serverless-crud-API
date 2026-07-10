from db import table 
from response import ok, error
from botocore.exceptions import ClientError

from typing import Any
from aws_lambda_typing.events import APIGatewayProxyEventV1

def delete_handler(event: APIGatewayProxyEventV1) -> dict[str, Any]:
    try:
        params = event.get("pathParameters") or {}
        note_id = params.get("id")
        if not note_id:
            return error(400, "Bad request.")
        response = table.delete_item(
            Key={
                "id": note_id
            },
            ReturnValues="ALL_OLD"
        )

        if "Attributes" not in response:
            return error(404, "Note not found.")

        return ok({"message": "Note deleted successfully."}, 200)
    except KeyError:
        return error(400, "Bad request.")
    except ClientError as e:
        return error(500, e.response["Error"]["Message"])