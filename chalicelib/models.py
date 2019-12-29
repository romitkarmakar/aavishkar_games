import uuid
import time
import random
import boto3
from utils import DecimalEncoder

dynamodb = boto3.resource(
    'dynamodb', region_name='ap-south-1')

class User:
    def __init__(self, sub):
        self.id = sub
        self.score = 0
        

class CLS:
    def __init__(self):
        self.id = "cls"

    def generate(self):
        self.numbers = []
        for i in range(5):
            self.numbers.append(random.randrange(1, 12, 1))


class Session:
    def __init__(self, gameId, player):
        self.id = str(uuid.uuid4())
        self.gameId = gameId
        self.players.append(player)
        self.timestamp = time.time()
        self.table = dynamodb.Table('aavishkar_sessions')
    
    def join(self, player):
        self.players.append(player)
    

