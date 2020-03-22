from telegram import Update
from telegram.ext import CallbackContext


def sure_filter(update: Update, context: CallbackContext) -> bool:
    words = update.effective_message.text.split()
    if "בטוח?" in words:
        msg = "ככה הבנתי"
        update.message.reply_text(msg)
        return True
    return False


# add any filter to this list.
# filters always recieve bot,update as arguments
# filters must either return False, or finish the job and return true
# they can send to another filter and return what that filter returned
filter_list = [
    sure_filter
]


def default_action(update: Update, context: CallbackContext) -> bool:
    msg = 'מה הכוונה?'
    update.message.reply_text(msg)


# just calls all the filters
def reply_filter(bot, update):
    for filter_func in filter_list:
        if filter_func(bot, update):
            break
    else:
        default_action(bot, update)
