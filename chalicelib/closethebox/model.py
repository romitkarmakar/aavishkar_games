import time
import random
import boto3
from ..utils import DecimalEncoder

dynamodb = boto3.resource(
    'dynamodb', region_name='ap-south-1')


class Session:
    def __init__(self, id=None):
        if id is not None:
            table = dynamodb.Table('aavishkargames_sessions')
            response = table.get_item(
                Key={
                    'game': 'closethebox',
                    'id': id
                }
            )
            self.state = response['Item']
