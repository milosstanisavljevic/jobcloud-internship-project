import boto3
from boto3.dynamodb.conditions import Key, Attr

table_name = 'kumo_crawler_job_ads_playground'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


def get_items():
    return table.scan(
        TableName=table_name
    )


def db_get_item_index(index, key, db_item):
    kwargs = {
        'IndexName': index,
        'KeyConditionExpression': Key(key).eq(db_item),
    }
    response = table.query(**kwargs)
    return response
