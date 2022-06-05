import asyncio, shutil, os, re
from pyrogram.types import *
from pyrogram import Client, filters
from lib.globals import ADMINS, PREFIXES, HelperID, Global
from pytgcalls.types import *
from pytgcalls.exceptions import NoAudioSourceFound, NoActiveGroupCall, GroupCallNotFound
from clients import calls

command = command = Global().get_commands(__file__)

@Client.on_message(filters.user(users=ADMINS) & filters.regex("^["+"\\".join(PREFIXES)+f"""]?({"|".join(command)})$""", re.U | re.I))
async def play(client: Client, message: Message):
    msg1 = await message.reply('**Please Wait ...**')
    if message.reply_to_message and message.reply_to_message.audio:
        path = await message.reply_to_message.download()
        title = f"{message.reply_to_message.audio.performer} - {message.reply_to_message.audio.title}"
        f_name = os.path.basename(path)
        path = shutil.move(path, 'queue/' + f_name)
        try:
            await calls.join_group_call(message.chat.id, AudioPiped(path))
            active_call = calls.get_active_call(message.chat.id)
            infos = await calls.get_participants(message.chat.id)
            for i in infos:
                if i.user_id == ADMINS[0]:
                    info = i
            if info.muted_by_admin == False:
                if active_call.is_playing == True:
                    msg = await client.get_inline_bot_results(HelperID, 'vcc_%s_%s_%s' %(message.chat.id, str(info.volume), title))
                    await message.reply_inline_bot_result(msg.query_id, msg.results[0].id)
                else:
                    await calls.leave_group_call(message.chat.id)
                await msg1.delete()
                await asyncio.sleep(message.reply_to_message.audio.duration)
                await calls.leave_group_call(message.chat.id)
                os.remove(path)
            else:
                await calls.leave_group_call(message.chat.id)
                await msg1.edit("Bot has been muted.")
        except (NoActiveGroupCall, NoAudioSourceFound, GroupCallNotFound, Exception) as e:
            await msg1.edit(e)
        






