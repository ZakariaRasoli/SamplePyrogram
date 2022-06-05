import time, re
from pyrogram.types import *
from pyrogram import Client, filters, enums
from lib.globals import ADMINS, PREFIXES, Global

command = command = Global().get_commands(__file__)

@Client.on_message(filters.user(users=ADMINS) & filters.regex("^["+"\\".join(PREFIXES)+f"""]?({"|".join(command)})$""", re.U | re.I))
async def ping(client: Client, message: Message):
    time0 = time.time()
    await client.send_chat_action(message.chat.id, enums.chat_action.ChatAction.TYPING)
    time1 = time.time()
    tm = round((time1 - time0) * 1000, 2)
    await message.reply(f'`Pong took {tm} ms.`')


