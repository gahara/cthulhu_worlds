import os
import json
from random import sample

from flask import render_template

from app import app, redis_conn
from app.docker.run_docker import run_docker_script


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


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


@app.route('/redis')
def check_redis():
    redis_conn.set('h1', '100')
    res = redis_conn.get('h1')
    return {
        'result': res.decode("utf-8").strip()
    }


