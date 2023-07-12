import boto3
import logging

table_name = 'kumo_crawler_job_ads_playground'
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(table_name)


class DynamoDB:

    def __init__(self, item):
        self.item = item

    def add_item(self):
        try:
            table.put_item(Item=self.item)
            logger = logging.getLogger('db')
            logger.setLevel(logging.DEBUG)
            logger.info(
                f'added job ad to database with id {self.item.get("id")} successfully')
        except Exception as e:
            logging.error(f'error on adding item to db', {e})

    def get_item(self):
        pass
