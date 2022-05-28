from pyrogram.types import *
from pyrogram import Client, filters, enums
import outputformat as ouf
from lib.globals import Global

prefixes = Global().prefixes()
admins = Global().admins()
command = Global().get_command(__file__)

@Client.on_message(filters.command(commands=command, prefixes=prefixes))
async def id(client: Client, message: Message):
    reply_to_message = message.reply_to_message
    if reply_to_message:
        reply_to_message_from_id = reply_to_message.from_user.id
        await idCommand(client ,message, reply_to_message_from_id)
    else:
        from_id = message.text.split(" ")[1] if len(message.text) > 4 else message.from_user.id
        await idCommand(client, message, from_id)


async def idCommand(client: Client, message: Message, from_id):
    chat = message.chat
    chat_id = chat.id
    try:
        user = await client.get_chat(from_id)
        cap1 = []
        en_type = enums.chat_type
        user_bot = [en_type.ChatType.PRIVATE, en_type.ChatType.BOT]
        other_chat = [en_type.ChatType.SUPERGROUP, en_type.ChatType.CHANNEL, en_type.ChatType.GROUP]
        if user.type in user_bot:
            cap1.append('**Firstname:** `%s`' %(user.first_name))
            if user.username: cap1.append('**Username:** `%s`' %(user.username))
            if user.last_name: cap1.append('**Lastname:** `%s`' %(user.last_name))
            if user.dc_id: cap1.append('**DC-ID:** `%s`' %(user.dc_id))
            cap1.append('**ID:** `%s`' %(user.id))
            cap1.append('**Status:** `%s`' %(message.from_user.status))
            if user.bio: cap1.append('**Bio:** `%s`' %(user.bio))
            cap1 = str(ouf.showlist(cap1, style="box", title="**User Info**", return_str=True))

            if chat.type == en_type.ChatType.SUPERGROUP:
                cap2 = []
                cap2.append('**Title:** `%s`' %(chat.title))
                cap2.append('**ID:** `%s`' %(chat_id))
                cap2 = str(ouf.showlist(cap2, style="box", title="**Chat Info**", return_str=True))
                cap1 = cap1 + cap2
                
        elif user.type in other_chat:
            cap1 = []
            cap1.append('**Title:** `%s`' %(user.title))
            cap1.append('**ID:** `%s`' %(user.id))
            if user.username: cap1.append('**Username:** `%s`' %(user.username))
            if user.dc_id: cap1.append('**DC-ID:** `%s`' %(user.dc_id))
            if user.members_count: cap1.append('**Members Count:** `%s`' %(user.members_count))
            if user.description: cap1.append('**Description:** `%s`' %(user.description))
            cap1 = str(ouf.showlist(cap1, style="box", title="**Chat Info**", return_str=True))
            
        if user.photo and user.type != en_type.ChatType.BOT:
            photos = []
            pics = []
            async for photo in client.get_chat_photos(from_id, 9):
                photos.append(photo.file_id)
            for photo in photos:
                if photo == photos[len(photos)-1]:
                    pics.append(InputMediaPhoto(photo, caption=cap1))
                else:
                    pics.append(InputMediaPhoto(photo))
            return await message.reply_media_group(pics)
        else:
            return await message.reply(cap1)
    except Exception as err:
        if message.from_user.id in admins:
            return await message.reply('**User** not Found.\n**Error:** `%s`' %(err))
        else:
            return await message.reply('**User** not Found.')





