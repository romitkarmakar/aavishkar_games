from chalice import Blueprint

to = Blueprint(__name__)


@to.route('/start')
def start():
    return {'foo': 'bar'}


@to.route('/join')
def join():
    return {'foo': 'bar'}


@to.route('/move', methods=['POST'])
def move():
    return {}
