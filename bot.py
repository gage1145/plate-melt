import os
from dotenv import load_dotenv
import logging
from signalbot import SignalBot, Command, Context, triggered, enable_console_logging

load_dotenv()


SIGNAL_SERVICE = os.getenv("SIGNAL_SERVICE")
PHONE_NUMBER = os.getenv("PHONE_NUMBER")

class PingCommand(Command):
    @triggered("Ping")
    async def handle(self, c: Context) -> None:
        await c.send("Pong")

if __name__ == "__main__":
    enable_console_logging(logging.INFO)

    bot = SignalBot({
        "signal_service": SIGNAL_SERVICE,
        "phone_number": PHONE_NUMBER
    })
    bot.register(PingCommand()) # Run the command for all contacts and groups
    bot.start()