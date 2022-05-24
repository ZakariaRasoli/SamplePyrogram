import os, io, sys, traceback
import time
from pyrogram import Client, emoji, enums
from pyrogram.types import Message


class Admin:
    def __init__(self, admins):
        self.admins = admins

    async def usageCommand(self, message: Message):
        import psutil
        process = psutil.Process(os.getpid())
        memory = self.get_size(process.memory_info().rss)
        em = emoji.CARD_INDEX_DIVIDERS
        await message.reply(f"{em} **Memory usage**: `{memory}`" )

    async def pingCommand(self, client: Client, message: Message):
        time0 = time.time()
        await client.send_chat_action(message.chat.id, enums.chat_action.ChatAction.TYPING)
        time1 = time.time()
        tm = round((time1 - time0) * 1000, 2)
        await message.reply(f'`Pong took {tm} ms.`')

    async def evalCommand(self, client: Client, message: Message, edit: Message = None):
        if edit:
            status_message = await edit.edit_text("`Processing ...`")
        else:
            status_message = await message.reply_text("`Processing ...`")
        cmd = message.text.split(" ", 1)[1]

        reply_to_ = message
        if message.reply_to_message:
            reply_to_ = message.reply_to_message

        final = await self.evaluation(cmd, client, message)
        if len(str(final)) > 4096:
            with io.BytesIO(str.encode(final)) as out_file:
                out_file.name = "eval.txt"
                await reply_to_.reply_document(document=out_file, caption=cmd, disable_notification=True)
                await status_message.delete()
        else:
            await status_message.edit_text(final)





    def get_size(self, bytes, suffix="B"):
        factor = 1024
        for unit in ["", "K", "M", "G", "T", "P"]:
            if bytes < factor:
                return f"{bytes:.2f}{unit}{suffix}"
            bytes /= factor

    async def evaluation(self, cmd, client, message):
        old_stderr = sys.stderr
        old_stdout = sys.stdout
        redirected_output = sys.stdout = io.StringIO()
        redirected_error = sys.stderr = io.StringIO()
        stdout, stderr, exc = None, None, None

        try:
            await self.aexec(cmd, client, message)
        except Exception:
            exc = traceback.format_exc()

        stdout = redirected_output.getvalue()
        stderr = redirected_error.getvalue()
        sys.stdout = old_stdout
        sys.stderr = old_stderr

        evaluation = ""
        if exc:
            evaluation = exc
        elif stderr:
            evaluation = stderr
        elif stdout:
            evaluation = stdout
        else:
            evaluation = "Success"

        final_output = "<b>Code</b>:\n"
        final_output += f"<code>{cmd}</code>\n\n"
        final_output += "<b>Outpot</b>:\n"
        final_output += f"<code>{evaluation.strip()}</code>\n"
        
        return final_output

    async def aexec(self, code, client, message):
        sys.tracebacklimit = 0
        exec(
            "async def __aexec(client, message): "
            + "".join(f"\n {l_}" for l_ in code.split("\n"))
        )
        return await locals()["__aexec"](client, message)
