import uuid
import time
import random
import boto3
from ..utils import DecimalEncoder

dynamodb = boto3.resource(
    'dynamodb', region_name='ap-south-1')


class Session:
    def __init__(self, player):
        self.id = str(uuid.uuid4())
        self.players.append(player)
        self.timestamp = time.time()
        table = dynamodb.Table('aavishkar_ctb')
        table.put_item(
            Item={
                'id': self.id,
                'players': self.players,
                'timestamp': self.timestamp
            }
        )

    def join(self, player):
        self.players.append(player)

    def isStarted(self):
        if len(self.players) > 1:
            return True
        else:
            return False

    def generate(self):
        self.numbers = []
        for i in range(5):
            self.numbers.append(random.randrange(1, 12, 1))
