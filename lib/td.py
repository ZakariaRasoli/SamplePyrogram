from pyrogram.types import *

def makeRowInlineKeyboard(data: list):
    result = []
    for i in data:
        result.append(InlineKeyboardButton(i[0], i[1]))
    return result

def makeInlineKeyboard(data: list):
    result = []
    for i in data:
        result.append(makeRowInlineKeyboard(i))
    return InlineKeyboardMarkup(result)

def answerArticleQuery(data: list):
    result = []
    for i in data:
        result.append(
            InlineQueryResultArticle(
                title=i[0], 
                input_message_content=InputTextMessageContent(i[1]), 
                description=i[2], 
                reply_markup=i[3],
            )
        )
    return result
