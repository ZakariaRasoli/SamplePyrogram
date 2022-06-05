import io, sys, traceback, re
from pyrogram.types import *
from pyrogram import Client, filters, enums
from lib.globals import ADMINS, PREFIXES, Global

command = command = Global().get_commands(__file__)

@Client.on_message(filters.user(users=ADMINS) & filters.regex("^["+"\\".join(PREFIXES)+f"""]?({"|".join(command)}) *(?:[\n\s]*)(.*)$""", re.U | re.I | re.S))
async def eval(client: Client, message: Message):
    await evalCommand(client, message)

@Client.on_message(filters.user(users=ADMINS) & filters.regex("^["+"\\".join(PREFIXES)+f"""]?({"|".join(command)}) *(?:[\n\s]*)(.*)$""", re.U | re.I | re.S))
async def editEval(client: Client, message: Message):
    msgs = []
    if message.chat.type in [enums.chat_type.ChatType.GROUP, enums.chat_type.ChatType.PRIVATE]:
        await evalCommand(client, message)
    else:
        async for msg in client.get_discussion_replies(message.chat.id, message.id):
            msgs.append(msg)
        msg_edit = msgs[len(msgs)-1]
        if msg_edit:
            await evalCommand(client, message, msg_edit)
        else:
            await evalCommand(client, message)




async def evalCommand(client: Client, message: Message, edit: Message = None):
    if edit:
        status_message = await edit.edit_text("`Processing ...`")
    else:
        status_message = await message.reply_text("`Processing ...`")
    cmd = message.matches[0].group(2)

    reply_to_ = message
    if message.reply_to_message:
        reply_to_ = message.reply_to_message

    final = await evaluation(cmd, client, message)
    if len(str(final)) > 4096:
        with io.BytesIO(str.encode(final)) as out_file:
            out_file.name = "eval.txt"
            await reply_to_.reply_document(document=out_file, caption=cmd, disable_notification=True)
            await status_message.delete()
    else:
        await status_message.edit_text(final)



    
async def evaluation(cmd, client, message):
    old_stderr = sys.stderr
    old_stdout = sys.stdout
    redirected_output = sys.stdout = io.StringIO()
    redirected_error = sys.stderr = io.StringIO()
    stdout, stderr, exc = None, None, None

    try:
        await aexec(cmd, client, message)
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

    final_output = "**Code**:\n"
    final_output += f"```{cmd}```\n\n"
    final_output += "**Output**:\n"
    final_output += f"```{evaluation.strip()}```\n"
    
    return final_output

async def aexec(code, client, message):
    sys.tracebacklimit = 0
    exec(
        "async def __aexec(client, message): "
        + "".join(f"\n {l_}" for l_ in code.split("\n"))
    )
    return await locals()["__aexec"](client, message)

    
