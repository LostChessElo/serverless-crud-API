import os
import boto3
import pytest
from moto import mock_aws


@pytest.fixture(scope="function")
def mock_credentials():
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "af-south-1"


@pytest.fixture(scope="function")
def dynamodb_mock(mock_credentials):
    with mock_aws():
        yield boto3.resource("dynamodb", region_name="af-south-1")


@pytest.fixture(scope="function")
def mock_table(dynamodb_mock):
    table = dynamodb_mock.create_table(
        TableName="notes",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}],
        BillingMode="PAY_PER_REQUEST",
    )
    table.meta.client.get_waiter("table_exists").wait(TableName="notes")
    return table
