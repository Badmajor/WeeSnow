import os

from environs import Env

env = Env()
env.read_env()

BOT_TOKEN = os.environ["BOT_TOKEN"]  # Забираем значение типа str

WEBHOOK_HOST = os.environ['WEBHOOK_HOST']
WEBHOOK_PATH = os.environ['WEBHOOK_PATH']
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"
WEBAPP_HOST = os.environ['WEBAPP_HOST']
WEBAPP_PORT = os.environ.get('PORT')

