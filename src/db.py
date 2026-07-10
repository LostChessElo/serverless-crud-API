import os 
import boto3 

def table():
    resource = boto3.resource("dynamodb", region_name="af-south-1")
    table = resource.Table("notes")
    return table
