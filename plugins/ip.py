import requests
from pyrogram.types import *
from pyrogram import Client, filters
from lib.globals import Global
import outputformat as ouf

prefixes = Global().prefixes()
admins = Global().admins()
command = Global().get_command(__file__)

@Client.on_message(filters.command(commands=command, prefixes=prefixes))
async def ip(client, message: Message):
    if len(message.text) > 4:
        await ipCommand(message)
    else:
        await message.reply('**ip or domain** not set.')


async def ipCommand(message: Message):
    ip = message.text.split(' ')[1]
    req = requests.get('http://ip-api.com/json/%s?fields=66846719' %(ip)).json()
    status = req['status']
    if status == 'success':
        title = '**IP**: `%s`' %(ip)
        msg = []
        if req['continent'] : msg.append('**Continent**: `%s`' %(req['continent']))
        if req['country'] : msg.append('**Country**: `%s`' %(req['country']))
        if req['regionName'] : msg.append('**Region Name**: `%s`' %(req['regionName']))
        if req['timezone'] : msg.append('**Timezone**: `%s`' %(req['timezone']))
        if req['isp'] : msg.append('**ISP**: `%s`' %(req['isp']))
        if req['asname'] : msg.append('**ASName**: `%s`' %(req['asname']))
        if req['query'] : msg.append('**Query**: `%s`' %(req['query']))
        msg = str(ouf.showlist(msg, style="line", title=title, return_str=True))
        await message.reply_location(req['lat'], req['lon'])
        return await message.reply_text(msg)
    else:
        return await message.reply('**ip** not Found.')
