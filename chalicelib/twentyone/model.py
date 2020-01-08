import random
import time

import boto3

dynamodb = boto3.resource(
    'dynamodb', region_name='ap-south-1')


class Session:
    def __init__(self, id=None):
        self.cards = []
        if id is not None:
            table = dynamodb.Table('aavishkargames_sessions')
            response = table.get_item(
                Key={
                    'game': 'twentyone',
                    'id': id
                }
            )
            self.state = response['Item']

    def start(self, email, amount):
        table = dynamodb.Table('aavishkargames_sessions')
        self.state = {
            "game": 'twentyone',
            "id":  '{}#{}'.format(email, str(time.time())),
            'amount': amount,
            'playerdata': {
                "score": [],
                "cards": []
            },
            'dealerdata': {
                "score": [],
                "cards": []
            },
            'currentMove': 'player',
            'winner': 'pending',
        }
        table.put_item(Item=self.state)
        self.hit('player')
        self.hit('player')
        self.hit('dealer')

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

        if len(self.score[side]) > 1:
            for index, score in enumerate(self.score[side]):
                if score > 21:
                    self.score[side].pop(index)

    def checkBust(self, side):
        if side == 'player':
            if self.score[side][0] > 21:
                self.winner = 'dealer'
            else:
                self.winner = 'player'
        else:
            if self.score[side][0] > 21:
                self.winner = 'player'
            else:
                self.winner = 'dealer'

    def hit(self, side=None):
        if side is None:
            side = self.currentMove
        card = self.generateCard()
        if self.cards[side].count(card) > 1:
            self.hit(side)
        self.cards[side].append(card)
        self.addScore(card, side)
        self.checkBust(side)
        if side == 'dealer':
            self.checkWinner()

    def stand(self):
        self.currentMove = 'dealer'

    def checkWinner(self):
        if self.score['dealer'] < 21:
            if self.score['dealer'] == self.score['player']:
                self.winner = 'draw'
            elif self.score['dealer'] > self.score['player']:
                self.winner = 'dealer'
            else:
                self.winner = 'player'
        elif self.score['dealer'] == 21:
            self.winner = 'dealer'
        else:
            self.winner = 'player'
