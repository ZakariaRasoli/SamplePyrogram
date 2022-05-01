from pyrogram.handlers import *
from modules.sendInfo import *
def messageHandler(app, admins, db):
    async def dump(client, message):
        await app.send_message(admins[1], message)
        

    myHandler = MessageHandler(dump)
    app.add_handler(myHandler)
