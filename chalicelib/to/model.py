import uuid
import time
import random
import boto3
from ..utils import DecimalEncoder

dynamodb = boto3.resource(
    'dynamodb', region_name='ap-south-1')


class Session:
    def __init__(self, id=None):
        table = dynamodb.Table('aavishkargames_sessions')
        if id is None:
            self.state = {
                "id": str(uuid.uuid4()),
                "timestamp": str(time.time()),
                "players": [],
                "game": 'twentyone',
                "gamedata": [],
                "currentmove": None
            }
            table.put_item(Item=self.state)
        else:
            response = table.get_item(
                Key={
                    'game': 'twentyone',
                    'id': id
                }
            )
            self.state = response['Item']

    def addPlayer(self, player):
        self.state['players'].append(player)
        self.state['gamedata'].append({
            "player": player,
            "cards": [],
            "score": 0
        })
        if self.state['currentmove'] is None:
            self.state['currentmove'] = player
        table = dynamodb.Table('aavishkargames_sessions')
        response = table.update_item(
            Key={
                'id': self.state["id"],
                'game': 'twentyone'
            },
            UpdateExpression="set players=:p, gamedata = :g, currentmove = :m",
            ExpressionAttributeValues={
                ':p': self.state['players'],
                ':g': self.state['gamedata'],
                ':m': self.state['currentmove']
            },
            ReturnValues="UPDATED_NEW"
        )

    def isStarted(self):
        if len(self.state['players']) > 1:
            return True
        else:
            return False

    def generateCard(self):
        colors = ['C', 'D', 'H', 'S']
        numbers = ['A', '2', '3', '4', '5', '6',
                   '7', '8', '9', '10', 'K', 'Q', 'J']
        number = random.randrange(0, len(numbers), 1)
        if number <= 10:
            self.score = number+1
        else:
            self.score = 10
        str = '{}{}'.format(colors[random.randrange(
            0, len(colors), 1)], numbers[number])
        return str

    def addCard(self, player):
        for data in self.state['gamedata']:
            if data['player'] == player:
                data['cards'].append(self.generateCard())
                data['score'] = data['score'] + self.score

        table = dynamodb.Table('aavishkargames_sessions')
        response = table.update_item(
            Key={
                'id': self.state["id"],
                'game': 'twentyone'
            },
            UpdateExpression="set gamedata = :g",
            ExpressionAttributeValues={
                ':g': self.state['gamedata']
            },
            ReturnValues="UPDATED_NEW"
        )

    def changeMove(self):
        currentValue = 0
        for index, player in enumerate(self.state['players']):
            if self.state['currentmove'] == player:
                currentValue = index

        if(currentValue == len(self.state['gamedata'])-1):
            self.state['currentmove'] = self.state['players'][0]
        else:
            self.state['currentmove'] = self.state['players'][currentValue + 1]

        table = dynamodb.Table('aavishkargames_sessions')
        response = table.update_item(
            Key={
                'id': self.state["id"],
                'game': 'twentyone'
            },
            UpdateExpression="set currentmove = :c",
            ExpressionAttributeValues={
                ':c': self.state['currentmove']
            },
            ReturnValues="UPDATED_NEW"
        )
