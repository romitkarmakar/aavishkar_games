from chalice import Blueprint

extra_routes = Blueprint(__name__)

@extra_routes.route('/start')
def foo():
    return {'foo': 'bar'}

@extra_routes.route('/join')
def foo():
    return {'foo': 'bar'}


