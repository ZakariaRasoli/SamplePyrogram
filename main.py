import asyncio, pyrogram, pytgcalls
from clients import cli, api, calls

async def main():
    apps = [cli, api]
    for app in apps:
        await app.start()
    await calls.start()
    await pyrogram.idle()
    await pytgcalls.idle()
    for app in apps:
        await app.stop()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
