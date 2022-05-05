from pyrogram import Client, enums
from pyrogram.types import *

from jdatetime import datetime as ds
from datetime import datetime


class Fun:
    def __init__(self, app: Client):
        self.app = app

    async def idCommand(self, message: Message, from_id):
        chat = message.chat
        chat_id = chat.id
        try:
            user = await self.app.get_chat(from_id)
            user2 = await self.app.get_users(from_id)
            if user.id:
                cap = '**User Info**\n ‌    ‍ ‌‌‌‌   **Firstname:** `%s`\n' %(user.first_name)
                if user.username:
                    cap += ' ‌    ‍ ‌‌‌‌   **Username:** `%s`\n' %(user.username)
                if user.last_name:
                    cap += ' ‌    ‍ ‌‌‌‌   **Lastname:** `%s`\n' %(user.last_name)
                if user.bio:
                    cap += ' ‌    ‍ ‌‌‌‌   **Bio:** `%s`\n' %(user.bio)
                if user.dc_id:
                    cap += ' ‌    ‍ ‌‌‌‌   **dc_id:** `%s`\n' %(user.dc_id)
                if user2.language_code:
                    cap += ' ‌    ‍ ‌‌‌‌   **Language Code:** `%s`\n' %(user2.language_code)
                
                cap += ' ‌    ‍ ‌‌‌‌   **ID:** `%s`\n' %(user.id) 
                cap += ' ‌    ‍ ‌‌‌‌   **Status:** `%s`\n' %(user2.status) 

                if chat.type == enums.chat_type.ChatType.SUPERGROUP:
                    cap += '**Group Info**\n ‌    ‍ ‌‌‌‌   **Title:** `%s`\n' %(chat.title)
                    cap += ' ‌    ‍ ‌‌‌‌   **ID:** `%s`\n' %(chat_id)
                
                if user.photo:
                    photos = []
                    pic = []
                    async for photo in self.app.get_chat_photos(from_id, 9):
                        photos.append(photo.file_id)
                    for photo in photos:
                        print(photo)
                        pic.append(InputMediaPhoto(photo, caption=cap))
                    await message.reply_media_group(pic)
                else:
                    await message.reply(cap)
        except Exception as err:
            await message.reply('**User** not Found.\n**Error:** `%s`' %(err))
            