import os
from pyrogram.types import *
from pyrogram import Client, filters
from lib.globals import Global


prefixes = Global().prefixes()
admins = Global().admins()
command = Global().get_command(__file__)

@Client.on_message(filters.user(users=admins) & filters.command(commands=command, prefixes=prefixes))
async def restart(client: Client, message: Message):
    await message.reply('`Bot Restarted.`')
    await os.execvp("python3.8",["python3.8","main.py",f"{message.chat.id}",f"{message.id}"])