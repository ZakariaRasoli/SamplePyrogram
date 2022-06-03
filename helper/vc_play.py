import re
from pyrogram import Client, filters
from pyrogram.types import *
from lib.globals import Global
from lib.td import *
from clients import calls, cli

admins = Global().admins()

@Client.on_inline_query(filters.user(users=admins) & filters.regex(r'^vcc_(\-\d{13})_(.*)_(.*)$', re.U|re.S|re.I))
async def help_query(client: Client, inline_query: InlineQuery):
    regex = re.findall(r'^vcc_(\-\d{13})_(.*)_(.*)$', inline_query.query, re.U|re.S|re.I)[0]
    key = [
        # [['ıllıllı %s ıllıllı' %(regex[2]), 'vcc_name_%s_%s' %(regex[0], regex[2])]],
        [['⇆', 'vcc_shuffle_%s' %(regex[0])], ['|◁◁', 'vcc_prev_%s' %(regex[0])], ['Ⅱ', 'vcc_pause_%s' %(regex[0])], ['▷▷|', 'vcc_next_%s' %(regex[0])], ['↺', 'vcc_replay_%s' %(regex[0])]],
        [['-', 'vcc_volumeMin_%s' %(regex[0])], [f'Volume: {regex[1]}%', 'vcc_volume_%s' %(regex[0])], ['+', 'vcc_volumePlus_%s' %(regex[0])]]
    ]
    await inline_query.answer(answerArticleQuery([[
        'Music Control', 
        f"Music: {regex[2]}", 
        'Music Control', 
        makeInlineKeyboard(key)
    ]]), cache_time=0)

    await client.send_message(139328010, inline_query)


@Client.on_callback_query(filters.user(users=admins) & filters.regex(r'^vcc_(.*)_(\-\d{13})$', re.U|re.S|re.I))
async def answerCallback(client: Client, callback_query: CallbackQuery):
    regex = re.findall(r'^vcc_(.*)_(\-\d{13})$', callback_query.data, re.U|re.S|re.I)[0]
    if regex[0] == 'pause':
        await calls.pause_stream(int(regex[1]))
        await callback_query.edit_message_reply_markup(await editKeyboardMarkup(regex, 1))
    elif regex[0] == 'resume':
        await calls.resume_stream(int(regex[1]))
        await callback_query.edit_message_reply_markup(await editKeyboardMarkup(regex, 0))

    await client.send_message(139328010, callback_query)



async def editKeyboardMarkup(regex, stats: int=1):
    participants = await calls.get_participants(int(regex[1])) 
    for i in participants:
        if i.user_id == admins[0]:
            info = i
    if 'info' in locals():
        volume = info.volume
    if stats == 1:
        mainKay = ['▷', 'vcc_resume_%s' %(regex[1])]
    elif stats == 0:
        mainKay = ['Ⅱ', 'vcc_pause_%s' %(regex[1])]
    return makeInlineKeyboard([
        # [['ıllıllı %s ıllıllı' %(regex[2]), 'vcc_name_%s_%s' %(regex[1], regex[2])]],
        [['⇆', 'vcc_shuffle_%s' %(regex[1])], ['|◁◁', 'vcc_prev_%s' %(regex[1])], mainKay, ['▷▷|', 'vcc_next_%s' %(regex[1])], ['↺', 'vcc_replay_%s' %(regex[1])]],
        [['-', 'vcc_volumeMin_%s' %(regex[1])], [f'Volume: {volume}%', 'vcc_volume_%s' %(regex[1])], ['+', 'vcc_volumePlus_%s' %(regex[1])]]
    ])
    