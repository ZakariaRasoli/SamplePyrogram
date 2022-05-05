import os, psutil
from pyrogram.types import Message
from pyrogram import Client, filters, errors, emoji
from pyrogram.raw import functions

from plugins.lib.fun import Fun

from plugins.lib.globals import Admins

prefixes = ["/", '!', '.', '#', '']
fun_commands = ['id']
admin_commands = ['usage']
admins = Admins.admins()

@Client.on_message(filters.command(commands=fun_commands, prefixes=prefixes))
async def fun(client, message: Message):
    command = message.command[0]
    reply_to_message = message.reply_to_message
    if command == 'id':
        if reply_to_message:
            reply_to_message_from_id = reply_to_message.from_user.id
            await Fun(client, admins).idCommand(message, reply_to_message_from_id)
        else:
            from_id = message.text.split(" ")[1] if len(message.text) > 4 else message.from_user.id
            await Fun(client, admins).idCommand(message, from_id)

@Client.on_message(filters.user(users=admins) & filters.command(commands=admin_commands, prefixes=prefixes))
async def admin(client, message: Message):
    command = message.command[0]
    if command == 'usage':
        process = psutil.Process(os.getpid())
        memory = get_size(process.memory_info().rss)
        em = emoji.CARD_INDEX_DIVIDERS
        await message.reply(f"{em} **Memory usage**: `{memory}`" )


def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
