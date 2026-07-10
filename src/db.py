import boto3
from mypy_boto3_dynamodb.service_resource import Table


def get_table() -> Table:
    resource = boto3.resource("dynamodb")
    return resource.Table("notes")


table = get_table()
