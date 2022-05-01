from pyrogram import Client
import configparser
from messageHandler import messageHandler
import mysql.connector as mysql

config = configparser.ConfigParser()
config.read('config.ini')

admins = []
for i in config['admins']:
    admins.append(config['admins'][i])

db = mysql.connect(
    host=config['database']['host'],
    database=config['database']['database'],
    user=config['database']['user'],
    password=config['database']['password'],
    use_unicode=True,
    charset='utf8mb4',
    connection_timeout=86400
)


app = Client(
    "my_online",
    api_id=config['pyrogram']['api_id'],
    api_hash=config['pyrogram']['api_hash']
)

messageHandler(app, admins, db)

app.run()