import os, psutil
from pyrogram.types import *
from pyrogram import Client, filters, emoji
from lib.globals import Global

prefixes = Global().prefixes()
admins = Global().admins()
command = Global().get_command(__file__)

@Client.on_message(filters.user(users=admins) & filters.command(commands=command, prefixes=prefixes))
async def usage(client: Client, message: Message):
    process = psutil.Process(os.getpid())
    memory = Global().get_size(process.memory_info().rss)
    em = emoji.CARD_INDEX_DIVIDERS
    await message.reply(f"{em} **Memory usage**: `{memory}`" )

