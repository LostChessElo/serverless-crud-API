from db import table
from response import ok, error 
from botocore.exceptions import ClientError
from typing import Any
from aws_lambda_typing.context import Context
from aws_lambda_typing.events import APIGatewayProxyEventV1

def get_handler(event: APIGatewayProxyEventV1, context: Context) -> dict[str, Any]:
    try:
        content = table.scan()["Items"]
        return ok(content)
    except ClientError as e:
        return error(500, "Could not fetch notes.")
