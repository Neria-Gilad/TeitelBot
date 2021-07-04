import logging
from typing import Callable, Any, Final

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import config

logger: Final = logging.getLogger(__name__)


class TelegramClient:
    def __init__(
        self,
        on_text: Callable[[str, Callable[[str], Any]], None],
        on_reply: Callable[[str, Callable[[str], Any]], None],
    ):
        self.updater = Updater(config.TOKEN, use_context=True)

        self._set_handlers(
            lambda update, _: on_text(
                update.effective_message.text, update.message.reply_text
            ),
            lambda update, _: on_reply(
                update.effective_message.text, update.message.reply_text
            ),
        )

        if config.IS_RUN_REMOTE:
            self._start_web_hook()
        else:
            self.updater.start_polling()

    def block_loop(self):
        self.updater.idle()

    def _start_web_hook(self):
        self.updater.start_webhook(
            listen="0.0.0.0", port=config.PORT, url_path=config.TOKEN
        )
        self.updater.bot.setWebhook(
            f"https://{config.APP_NAME}.herokuapp.com/{config.TOKEN}"
        )

    def _set_handlers(self, on_text, on_reply):
        dispatcher = self.updater.dispatcher
        dispatcher.add_handler(
            CommandHandler("start", lambda update, _: update.message.reply_text("מה"))
        )
        dispatcher.add_handler(MessageHandler(Filters.reply, on_reply))
        dispatcher.add_handler(MessageHandler(Filters.text, on_text))
        dispatcher.add_error_handler(
            lambda update, _, err: logger.error(
                'Update "%s" caused error "%s"', update, err
            )
        )
