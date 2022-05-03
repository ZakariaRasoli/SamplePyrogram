from pyrogram.handlers import *


def messageHandler(app, admins):
    async def dump(client, message):
        await app.send_message(admins[1], message)
        

    myHandler = MessageHandler(dump)
    app.add_handler(myHandler)
