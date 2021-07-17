import os
import json

from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/random')
def random():
    data = {}
    cards_path = os.path.join(app.static_folder, 'resources', 'cards.json')
    with open(cards_path) as cards:
        data = json.load(cards)

    return {'cards': data}
