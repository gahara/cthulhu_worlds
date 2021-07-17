import os
import json

from random import sample

from app import app
from app.docker.run_docker import run_docker_script


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


@app.route('/start')
def start():
    res = run_docker_script()

    return {'container_id': res}

