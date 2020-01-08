from chalice import Blueprint
from chalicelib.twentyone.model import Session
from chalice.app import Response
sevenup = Blueprint(__name__)


@sevenup.route('/start', methods=['POST'])
def start():
    request_body = sevenup.current_request.json_body
    if request_body:
        session = Session()
        session.create(request_body['player'], request_body['amount'])
        return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)

@sevenup.route('/hit/{sessionId}', methods=['POST', 'PUT'])
def hit(sessionId):
    request_body = sevenup.current_request.json_body
    if request_body:
        session = Session(sessionId)
        # session.addCard('player', session.generateCard())
    return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)


@sevenup.route('/stand/{sessionId}', methods=['POST', 'PUT'])
def stand(sessionId):
    request_body = sevenup.current_request.json_body
    if request_body:
        session = Session(sessionId)
        # session.addCard('dealer', session.generateCard())
    return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)
