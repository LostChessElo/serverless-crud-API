import json 
from db import table 
from typing import Any
from aws_lambda_typing.context import Context
from aws_lambda_typing.events import APIGatewayProxyEventV1

def get_handler(event: APIGatewayProxyEventV1, context: Context) -> dict[str, Any]:
    pass