from pyrogram.handlers import *


def messageHandler(app, admins):
    async def dump(client, message):
        await app.send_message(admins[0], message)
        

    myHandler = MessageHandler(dump)
    app.add_handler(myHandler)
