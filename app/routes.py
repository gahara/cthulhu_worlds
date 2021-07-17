import os
import json

from random import sample

from app import app


@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/random')
def random():
    cards = {}
    cards_path = os.path.join(app.static_folder, 'resources', 'cards.json')
    with open(cards_path) as raw_cards:
        cards = json.load(raw_cards)

    result = [cards[i] for i in sample(range(len(cards)), 3)]

    return {'cards': result}
