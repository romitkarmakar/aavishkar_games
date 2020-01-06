import uuid
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
                    'game': 'twentyone',
                    'id': id
                }
            )
            self.state = response['Item']

    def create(self, player, amount):
        table = dynamodb.Table('aavishkargames_sessions')
        self.state = {
            "id": str(uuid.uuid4()),
            "timestamp": str(time.time()),
            "game": 'twentyone',
            'player': player,
            'amount': amount,
            'winner': 'pending'
        }
        table.put_item(Item=self.state)

    def generateCard(self):
        self.score = []
        colors = ['C', 'D', 'H', 'S']
        numbers = ['A', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'K', 'Q', 'J']

        str = '{}{}'.format(colors[random.randrange(
            0, len(colors), 1)], numbers[random.randrange(0, len(numbers), 1)])
        return str

    def addScore(self, card, side):
        number = ord(card[-1])
        if number > 65 and number < 90:
            if number == 65:
                if len(self.score[side]) > 1:
                    temp = min(self.score[side])
                    self.score[side][0] = temp + 1
                    self.score[side][1] = temp + 11
                else:
                    temp = self.score[side][0]
                    self.score[side][0] += 1
                    self.score[side][1] = temp + 11
            else:
                self.score[side] = [i+10 for i in self.score[side]]
        else:
            temp = int(number)
            self.score[side] = [i+temp for i in self.score[side]]
        
        for index, score in enumerate(self.score[side]):
            if score > 21:
                self.score[side].pop(index)

    def hit(self, side):
        pass

    def checkWinner(self):
        pass


