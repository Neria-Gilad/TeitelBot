import response

import startup
from client.telegram_client import TelegramClient


def main():
    startup.init()

    client = TelegramClient(response.reply.on_message, response.quote.on_message)
    client.block_loop()


if __name__ == "__main__":
    main()
