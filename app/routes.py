import os
import json
from random import sample

from flask import render_template, request

from app import app, redis_conn
from app.docker.run_docker import run_docker_script

CARDS_HASH_NAME = '_cards'


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


@app.route('/create_container')
def create_container():
    res = run_docker_script()

    return {'container_id': res}


@app.route('/load_cards')
def load_cards():
    cards_path = os.path.join(app.static_folder, 'resources', 'cards.json')
    with open(cards_path) as raw_cards:
        cards = json.load(raw_cards)

    [redis_conn.hset(CARDS_HASH_NAME, card['title'],
                     json.dumps(card['effects'])) for card in cards]

    return 'OK'


@app.route('/redis', methods=['GET'])
def redis_get():
    if request.args.get('cards'):
        raw_cards = redis_conn.hgetall(CARDS_HASH_NAME)
        presentable = []

        for k, v in raw_cards.items():
            presentable.append({k: json.loads(v)})
        return {
            'result': presentable
        }

    key = request.args.get('key')
    value = redis_conn.get(key)

    return {
        'result': value.decode("utf-8").strip()
    }


@app.route('/redis', methods=['POST'])
def redis_set():
    key = request.json['key']
    value = request.json['value']
    redis_conn.set(key, value)

    return {
        'result': f'set {key}={value}'
    }
