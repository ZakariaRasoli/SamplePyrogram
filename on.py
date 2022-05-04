from pyrogram import Client
import configparser
from messageHandler import messageHandler

config = configparser.ConfigParser()
config.read('config.ini')

admins = []
for i in config['admins']:
    admins.append(int(config['admins'][i]))

app = Client(
    "my_online",
    api_id=config['pyrogram']['api_id'],
    api_hash=config['pyrogram']['api_hash'],
)

messageHandler(app, admins)

app.run()
