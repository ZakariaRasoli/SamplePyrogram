from pyrogram import Client, enums
from pyrogram.types import *

from jdatetime import datetime as ds
from datetime import datetime


class Fun:
    def __init__(self, app: Client, admins):
        self.app = app
        self.admins = admins

    async def idCommand(self, message: Message, from_id):
        chat = message.chat
        chat_id = chat.id
        try:
            user = await self.app.get_chat(from_id)
            user2 = await self.app.get_users(from_id)
            cap1 = []
            if user.id:
                cap1.append('**Firstname:** `%s`' %(user.first_name))
                if user.username:
                    cap1.append('**Username:** `%s`' %(user.username))
                if user.last_name:
                    cap1.append('**Lastname:** `%s`' %(user.last_name))
                if user.bio:
                    cap1.append('**Bio:** `%s`' %(user.bio))
                if user.dc_id:
                    cap1.append('**dc_id:** `%s`' %(user.dc_id))
                if user2.language_code:
                    cap1.append('**Language Code:** `%s`' %(user2.language_code))
                
                cap1.append('**ID:** `%s`' %(user.id))
                cap1.append('**Status:** `%s`' %(user2.status))
                import outputformat as ouf
                cap1 = str(ouf.showlist(cap1, style="box", title="**User Info** ‌    ‍ ‌", return_str=True))
 
                if chat.type == enums.chat_type.ChatType.SUPERGROUP:
                    cap2 = []
                    cap2.append('**Title:** `%s`' %(chat.title))
                    cap2.append('**ID:** `%s`' %(chat_id))
                    cap2 = str(ouf.showlist(cap2, style="box", title="**Group Info** ‌    ‍ ‌", return_str=True))
                    cap1 = cap1 + cap2
                if user.photo:
                    photos = []
                    pic = []
                    async for photo in self.app.get_chat_photos(from_id, 9):
                        photos.append(photo.file_id)
                    for photo in photos:
                        if photo == photos[len(photos)-1]:
                            pic.append(InputMediaPhoto(photo, caption=cap1))
                        else:
                            pic.append(InputMediaPhoto(photo))
                    await message.reply_media_group(pic)
                else:
                    await message.reply(cap1)
        except Exception as err:
            if message.from_user.id in self.admins:
                await message.reply('**User** not Found.\n**Error:** `%s`' %(err))
            else:
                await message.reply('**User** not Found.')
