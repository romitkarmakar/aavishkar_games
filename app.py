from chalice import Chalice
from chalicelib.closethebox.controller import extra_routes
from chalicelib.twentyone.controller import to

app = Chalice(app_name='aavishkar-games')
app.experimental_feature_flags.update([
    'WEBSOCKETS',
    'BLUEPRINTS'
])
app.debug = True
app.api.cors = True

@app.route('/')
def index():
    return {'hello': 'world'}


app.register_blueprint(extra_routes, url_prefix='/ctb')
app.register_blueprint(to, url_prefix='/to')
