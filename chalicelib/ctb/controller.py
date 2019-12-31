from chalice import Blueprint

extra_routes = Blueprint(__name__)


@extra_routes.route('/start')
def start():
    return {'foo': 'bar'}


@extra_routes.route('/join')
def join():
    return {'foo': 'bar'}

@extra_routes.route('/move', methods=['POST'])
def move():
    return {}
