from chalice import Blueprint
from chalicelib.twentyone.model import Session
from chalice.app import Response
twentyone = Blueprint(__name__)


@twentyone.route('/start', methods=['POST'])
def start():
    request_body = twentyone.current_request.json_body
    if request_body:
        session = Session()
        session.start(request_body['player'], request_body['amount'])
        return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)

@twentyone.route('/hit/{sessionId}', methods=['POST', 'PUT'])
def hit(sessionId):
    request_body = twentyone.current_request.json_body
    if request_body:
        session = Session(sessionId)
        session.hit()
    return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)


@twentyone.route('/stand/{sessionId}', methods=['POST', 'PUT'])
def stand(sessionId):
    request_body = twentyone.current_request.json_body
    if request_body:
        session = Session(sessionId)
        session.stand()
    return Response(status_code=201, headers={'Content-Type': 'application/json'}, body=session.state)
