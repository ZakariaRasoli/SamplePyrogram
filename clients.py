import pyrogram
import pytgcalls
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

plugins = dict(root='plugins')

helper_plugin = dict(root='helper')

cli = pyrogram.Client(
    config['clients']['cli'],
    api_id=config['pyrogram']['api_id'],
    api_hash=config['pyrogram']['api_hash'],
    plugins=plugins
)

api = pyrogram.Client(
    config['clients']['api'],
    api_id=config['pyrogram']['api_id'],
    api_hash=config['pyrogram']['api_hash'],
    bot_token=config['pyrogram']['token'],
    plugins=helper_plugin
)

calls = pytgcalls.PyTgCalls(cli, cache_duration=100, overload_quiet_mode=True)