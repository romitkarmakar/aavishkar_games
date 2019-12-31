from chalice import Blueprint
from chalicelib.to.model import Session
from chalice.app import Response
to = Blueprint(__name__)


@to.route('/start', methods=['POST'])
def start():
    request_body = to.current_request.json_body
    if request_body:
        session = Session()
        session.addPlayer(request_body['player'])
        return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)


@to.route('/join/{sessionId}', methods=['PUT', 'POST'])
def join(sessionId):
    request_body = to.current_request.json_body
    if request_body:
        session = Session(sessionId)
        session.addPlayer(request_body['player'])
        return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)


@to.route('/hit/{sessionId}', methods=['POST'])
def hit(sessionId):
    request_body = to.current_request.json_body
    if request_body:
        session = Session(sessionId)
        session.addCard(request_body['player'])
    return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)


@to.route('/stand/{sessionId}', methods=['POST', 'PUT'])
def stand(sessionId):
    request_body = to.current_request.json_body
    if request_body:
        session = Session(sessionId)
        if request_body['player'] == session.state['currentmove']:
            session.changeMove()
    return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)


@to.route('/deal')
def deal():
    return {}
