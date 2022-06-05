import os, psutil, re
from pyrogram.types import *
from pyrogram import Client, filters, emoji
from lib.globals import ADMINS, PREFIXES, Global
from lib.functions import get_size

command = command = Global().get_commands(__file__)

@Client.on_message(filters.user(users=ADMINS) & filters.regex("^["+"\\".join(PREFIXES)+f"""]?({"|".join(command)})$""", re.U | re.I))
async def usage(client: Client, message: Message):
    process = psutil.Process(os.getpid())
    memory = get_size(process.memory_info().rss)
    em = emoji.CARD_INDEX_DIVIDERS
    await message.reply(f"{em} **Memory usage**: `{memory}`" )

