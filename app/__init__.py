import os

from flask import Flask
import redis
from config import Config
from app.settings import REDIS_URI

app = Flask(__name__, static_folder='static')
app.config.from_object(Config)

redis_conn = redis.Redis(
    host=os.getenv("REDIS_HOST", "127.0.0.1"),
    port=os.getenv("REDIS_PORT", "6379"))

from app import routes