import time
from pyrogram.types import *
from pyrogram import Client, filters, enums
from lib.globals import Global

prefixes = Global().prefixes()
admins = Global().admins()
command = Global().get_command(__file__)

@Client.on_message(filters.user(users=admins) & filters.command(commands=command, prefixes=prefixes))
async def ping(client: Client, message: Message):
    time0 = time.time()
    await client.send_chat_action(message.chat.id, enums.chat_action.ChatAction.TYPING)
    time1 = time.time()
    tm = round((time1 - time0) * 1000, 2)
    await message.reply(f'`Pong took {tm} ms.`')


