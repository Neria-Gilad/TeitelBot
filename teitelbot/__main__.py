import response

import startup
from client.telegram_client import TelegramClient


def main():
    startup.init()

    client = TelegramClient(response.on_message, response.on_quote)
    client.block_loop()


if __name__ == "__main__":
    main()
