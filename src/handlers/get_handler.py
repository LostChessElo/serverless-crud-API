from db import table
from response import ok, error
from botocore.exceptions import ClientError

from typing import Any


def get_handler() -> dict[str, Any]:
    try:
        content: list[dict[str, Any]] = table.scan()["Items"]
        return ok(content)
    except ClientError as e:
        return error(500, e.response["Error"]["Message"])
