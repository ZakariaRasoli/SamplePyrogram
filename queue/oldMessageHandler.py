from time import sleep
from pyrogram.handlers import *
from pyrogram import filters
from modules.sendInfo import *

def messageHandler(app, admins, db):
    async def dump(client, message):
        # await app.send_message(139328010, message)
        from_user = message.from_user
        message_id = message.id
        chat = message.chat
        from_id = from_user.id
        chat_id = chat.id
        text = message.text
        reply_to_message = message.reply_to_message
        if text == '!id':
            if reply_to_message:
                reply_to_message_from_id = reply_to_message.from_user.id
                await sendInfo(app, admins, db).GroupUser(chat, reply_to_message_from_id)
            else:
                await sendInfo(app, admins, db).GroupUser(chat, from_id)
        elif text.split(" ")[0] == '!id' and text.split(" ", 1)[1]:
            await sendInfo(app, admins, db).GroupUser(chat, text.split(" ")[1])
        elif text == '!date':
            await sendInfo(app, admins, db).sendDateInfo(chat_id)
        elif text.split(' ')[0] == '!w' and text.split(' ', 1)[1]:
            await sendInfo(app, admins, db).weatherOneCall(chat_id, from_id, text.split(' ', 1)[1])
        elif text.split(' ')[0] == '!whois' and text.split(' ')[1]:
            await sendInfo(app, admins, db).whoIs(chat_id, from_id, text.split(' ', 1)[1])
        elif text.split(" ")[0] == '!ip' and text.split(" ", 1)[1]:
                await sendInfo(app, admins, db).IPInfo(chat_id, text.split(" ", 1)[1])

        if str(from_id) in admins:
            if text == 'test':
                await message.reply("**Hello** __baby__.")
                # async for message in app.search_messages(chat_id, query="سلام", limit=50):
                #     await message.forward(chat_id)
                #     sleep(0.2)
            elif text == '!stop':
                await message.reply(app.stop())
                # app.stop()

            elif text == '!restart':
                msg = await message.reply("Restarting ...")
                app.restart()
                sleep(1)
                await msg.edit_text("**Restarted** ...")



    myHandler = MessageHandler(dump, filters=filters.channel|filters.group)
    app.add_handler(myHandler)