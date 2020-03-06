from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import string


names = {"@Teitelbot"}


def updateArray(msg):
    if msg.from_user and msg.from_user.username:
        if ('@' + msg.from_user.username) not in names:
            names.add('@' + msg.from_user.username)
            with open("names.txt", mode='a') as namefile:
                namefile.write('@' + msg.from_user.username.strip() + '\n')


def initNamesFile():
    with open("names.txt", mode='r') as namefile:
        for name in namefile:
            names.add(name.strip())


def getMail(msg):
    mail = msg.split(u"מייל של ", 1)
    if len(mail) == 1:
        mail = msg.split(u"מייל", 1)
    mail = mail[1]
    if len(mail) == 0 or msg == u"מייל של":
        return "של מי"
    if len(mail.split()) > 4 or len(mail.split()) == 0:
        return ""
    translator = Translator()
    return cleanPunctuation(translator.translate(mail, src='iw', dest='en').text.lower().replace(" ", "")) + "@g.jct.ac.il"


def having(msg):
    words = cleanPunctuation(msg).split()
    i = 0
    for w in words:
        if w == u"יש" or w == u"אין":
            break
        else:
            i = i+1

    words = words[i:]

    words = [w.replace(u"אין", u"127635~~`;") for w in words]
    words = [w.replace(u"יש", u"אין") for w in words]
    words = [w.replace(u"127635~~`;", u"יש") for w in words]
    words = [w.replace(u"לי", u";;11;;11~234~") for w in words]
    words = [w.replace(u"לך", u"לי") for w in words]
    words = [w.replace(u";;11;;11~234~", u"לך") for w in words]
    return ' '.join(words)


def start(bot, update):
    update.message.reply_text('')


def reply(bot, update):
    text = update.message.text
    msg = ""
    if ("בטוח?" in text.split()):
        msg = "ככה הבנתי"
    if msg != "":
        update.message.reply_text(msg)


def echo(bot, update):
    updateArray(update.message)
    tmp = update.message.text
    msg = ""
    if(u"דחוף!" in tmp.split()):
        msg = "זה ממש דחוף תעזרו לו!"
    elif(u"מייל" in tmp):
        msg = getMail(tmp)
    elif(u"יש למישהו" in tmp or u"למישהו יש" in tmp or u"למישו יש" in tmp or u"יש למישו" in tmp):
        msg = "מישהו אמר לי אתמול שיש לו מלא"
    elif(u"יש" in tmp.split() or u"אין" in tmp.split()):
        msg = having(tmp)  # "אין"
    elif (u"מה" in tmp.split()):
        msg = "אל תגיד לי מה"
    elif (u"למה" in tmp.split()):
        msg = "for the glory of satan, of course!"
    elif(u"האם" == tmp.split()[0]):
        msg = u"פעם חשבתי שכן"
    elif(u"?" in tmp):
        msg = "אני לא מאמין ששאלת את זה"
    elif(u"שמות" in tmp):
        for n in names:
            msg += n + ' '
    elif(u"5.5" == tmp.split()[0] and len(tmp) == 3):
        msg = u"שראל שתוק!"
    else:
        try:
            f = float(tmp)
            if f > 11803.06 and f < 11803.07:
                msg = u"שראל שתוק!"
        except ValueError:
            pass
    if msg != "":
        update.message.reply_text(msg)


def error(bot, update, error):
    logger.warn('Update "%s" caused error "%s"' % (update, error))


def main():
    # Create the EventHandler and pass it your bot's token.
    updater = Updater(TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))

    # # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.reply, reply))
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Init names list
    initNamesFile()

    # Start the Bot
    updater.start_polling()

    # Run the bot until the you presses Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT.  This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()
