from pyrogram import Client, filters, emoji
from pyrogram.types import Message

def messageHandler(app: Client, admins):
    prefixes = ["/", '!', '.', '#']
    fun_commands = ['id']
    admin_commands = ['usage']
    
    @app.on_message(filters=filters.command(commands=fun_commands, prefixes=prefixes))
    async def fun(client, message: Message):
        command = message.command[0]
        if command == 'id':
            await message.reply("**%s**\n`%d`" %(message.from_user.first_name, message.from_user.id))

    @app.on_message(filters=filters.user(users=admins) & filters.command(commands=admin_commands, prefixes=prefixes))
    async def admin(client, message: Message):
        command = message.command[0]
        if command == 'usage':
            memory = memory_usage()['rss']
            em = emoji.CARD_INDEX_DIVIDERS
            await message.reply(f"{em} **Memory usage**: `{memory}`" )


def memory_usage():
    status = None
    result = {'peak': 0, 'rss': 0}
    try:
        status = open('/proc/self/status')
        for line in status:
            parts = line.split()
            key = parts[0][2:-1].lower()
            if key in result:
                result[key] = get_size(int(parts[1]) * 1024)
    finally:
        if status is not None:
            status.close()
    return result

def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
