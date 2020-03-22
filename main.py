import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from echo_filter import echo_filter
from reply_filter import reply_filter

import startup
import config


def start(update, context):
    update.message.reply_text("Hi!")


def error(update, context, err):
    logger = logging.getLogger(__name__)
    logger.warning('Update "%s" caused error "%s"', update, err)


def start_web_hook(update):
    update.start_webhook(listen="0.0.0.0",
                         port=int(config.PORT),
                         url_path=config.TOKEN)
    update.bot.setWebhook(
        f"https://{config.NAME}.herokuapp.com/{config.TOKEN}")


def add_handlers(dispatcher):
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(MessageHandler(Filters.reply, reply_filter))
    dispatcher.add_handler(MessageHandler(Filters.text, echo_filter))
    dispatcher.add_error_handler(error)


if __name__ == "__main__":
    startup.init()

    updater = Updater(config.TOKEN, use_context=True)

    add_handlers(updater.dispatcher)

    if config.IS_RUN_REMOTE:
        start_web_hook(updater)
    else:
        updater.start_polling()

    updater.idle()

# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
# from googletrans import Translator
# import string
#
# names = {"@Teitelbot"}
#
#
# def updateArray(msg):
#     if msg.from_user and msg.from_user.username:
#         if ('@' + msg.from_user.username) not in names:
#             names.add('@' + msg.from_user.username)
#             with open("names.txt", mode='a') as namefile:
#                 namefile.write('@' + msg.from_user.username.strip() + '\n')
#
#
# def cleanPunctuation(str):
#     for p in string.punctuation:
#         str = str.replace(p, "")
#     return str
#
#
# def initNamesFile():
#     with open("names.txt", mode='r') as namefile:
#         for name in namefile:
#             names.add(name.strip())
#
#
# def reply(bot, update):
#     tmp = update.message.text
#     msg = ""
#     if (u"בטוח?" in tmp.split()):  msg = "ככה הבנתי"
#     if msg != "":
#         update.message.reply_text(msg)
#
#
# def echo(bot, update):
#     updateArray(update.message)
#     tmp = update.message.text
#     msg = ""
#     if (u"דחוף!" in tmp.split()):
#         msg = "זה ממש דחוף תעזרו לו!"
#     elif (u"מייל" in tmp):
#         msg = getMail(tmp)
#     elif (u"יש למישהו" in tmp or u"למישהו יש" in tmp or u"למישו יש" in tmp or u"יש למישו" in tmp):
#         msg = "מישהו אמר לי אתמול שיש לו מלא"
#     elif u"יש" in tmp.split() or u"אין" in tmp.split():
#         msg = having(tmp)  # "אין"
#     elif (u"מה" in tmp.split()):
#         msg = "אל תגיד לי מה"
#     elif (u"למה" in tmp.split()):
#         msg = "for the glory of satan, of course!"
#     elif (u"האם" == tmp.split()[0]):
#         msg = u"פעם חשבתי שכן"
#     elif (u"?" in tmp):
#         msg = "אני לא מאמין ששאלת את זה"
#     elif (u"שמות" in tmp):
#         for n in names:
#             msg += n + ' '
#     elif (u"5.5" == tmp.split()[0] and len(tmp) == 3):
#         msg = u"שראל שתוק!"
#     else:
#         try:
#             f = float(tmp)
#             if f > 11803.06 and f < 11803.07:
#                 msg = u"שראל שתוק!"
#         except ValueError:
#             msg = ""
#     if msg != "":
#         update.message.reply_text(msg)
#
#
# def error(bot, update, error):
#     # logger.warn('Update "%s" caused error "%s"' % (update, error))
#     pass
#
#