from chalice import Chalice
from chalicelib.twentyone.controller import twentyone

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


app.register_blueprint(twentyone, url_prefix='/twentyone')
