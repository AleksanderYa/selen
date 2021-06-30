from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler


updater = Updater(token='1841807907:AAFgZgg766DoELrN-W4EHmtGVO6pGot7GrA', use_context=True)


def start(update, context):
    text_caps = ' '.join(context.args) + '? All good!'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)


def stop(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Iam OFF")
    updater.stop()

    def inline_caps(update, context):
        query = update.inline_query.query
        if not query:
            return
        results = list()
        results.append(
            InlineQueryResultArticle(
                id=query.upper(),
                title='Caps',
                input_message_content=InputTextMessageContent(query.upper())
            )
        )
        context.bot.answer_inline_query(update.inline_query.id, results)

    def caps(update, context):
        text_caps = ' '.join(context.args).upper()
        context.bot.send_message(chat_id=update.effective_chat.id, text=text_caps)

    start_handler = CommandHandler('start', start)
    updater.dispatcher.add_handler(start_handler)

    updater.start_polling()

    updater.stop()

    start_handler = CommandHandler('stop', stop)
    updater.dispatcher.add_handler(start_handler)

    caps_handler = CommandHandler('caps', caps)
    updater.dispatcher.add_handler(caps_handler)

    inline_caps_handler = InlineQueryHandler(inline_caps)
    updater.dispatcher.add_handler(inline_caps_handler)