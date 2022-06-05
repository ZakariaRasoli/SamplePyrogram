import os, re
from pyrogram.types import *
from pyrogram import Client, filters
from lib.globals import ADMINS, PREFIXES, Global

command = command = Global().get_commands(__file__)

@Client.on_message(filters.user(users=ADMINS) & filters.regex("^["+"\\".join(PREFIXES)+f"""]?({"|".join(command)})$""", re.U | re.I))
async def restart(client: Client, message: Message):
    await message.reply('`Bot Restarted.`')
    await os.execvp("python3.8",["python3.8","main.py",f"{message.chat.id}",f"{message.id}"])