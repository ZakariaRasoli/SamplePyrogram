from pyrogram.types import Message
from pyrogram import Client, filters, errors, emoji
from pyrogram.raw import functions

from plugins.lib.globals import Admins

prefixes = ["/", '!', '.', '#', '']
fun_commands = ['id']
admin_commands = ['usage', 'ping', 'eval']
admins = Admins.admins()

@Client.on_message(filters.command(commands=fun_commands, prefixes=prefixes))
async def fun(client, message: Message):
    from plugins.lib.fun import Fun
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
    from plugins.lib.admin import Admin
    command = message.command[0]
    if command == 'usage':
        await Admin(admins).usageCommand(message)
    elif command == 'ping':
        await Admin(admins).pingCommand(message)
    elif command == 'eval':
        await Admin(admins).evalCommand(client, message)

@Client.on_edited_message(filters.user(users=admins) & filters.command(commands=admin_commands, prefixes=prefixes))
async def editAdmin(client: Client, message: Message):
    from plugins.lib.admin import Admin
    command = message.command[0]
    if command == 'eval':
        msgs = []
        async for msg in client.get_discussion_replies(message.chat.id, message.id):
            msgs.append(msg)
        msg_edit = msgs[len(msgs)-1]
        await Admin(admins).evalCommand(client, message, msg_edit)
