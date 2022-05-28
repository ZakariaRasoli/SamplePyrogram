from pyrogram import Client
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

plugins = dict(root='plugins')

Client(
    "my_online",
    api_id=config['pyrogram']['api_id'],
    api_hash=config['pyrogram']['api_hash'],
    plugins=plugins
).run()
