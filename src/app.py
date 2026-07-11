from response import error
from get_handler import get_handler
from post_handler import post_handler
from patch_handler import patch_handler
from delete_handler import delete_handler

from typing import TYPE_CHECKING, Any
if TYPE_CHECKING:
    from aws_lambda_typing.events import APIGatewayProxyEventV1
    from aws_lambda_typing.context import Context


def handler(event: "APIGatewayProxyEventV1", context: "Context") -> dict[str, Any]:
    match event.get("httpMethod"):
        case "GET":
            return get_handler()
        case "POST":
            return post_handler(event, context)
        case "PATCH":
            return patch_handler(event)
        case "DELETE":
            return delete_handler(event)
        case _:
            return error(405, "Method not allowed.")
