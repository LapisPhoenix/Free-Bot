# Bot written by: Lapis Pheonix#2194
# Support Me: https://lapispheonix.com
# Want more bots? https://discord.gg/mWSRTKTvMq


import logging
import logging.handlers
import sys
from pathlib import Path

import discord
from discord.ext import commands

import settings
from database import create_database


def setup_logging():
    # Logging credit: Fretgfr
    log_fmt = logging.Formatter(
        fmt="%(asctime)s - %(name)s:%(lineno)d - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    sh = logging.StreamHandler(sys.stdout)
    sh.setLevel(logging.DEBUG)
    sh.setFormatter(log_fmt)

    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    root_logger.addHandler(sh)


_logger = logging.getLogger(__name__)


class MyBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(
            command_prefix=settings.prefix,
            description=settings.description,
            intents=discord.Intents.all(),
            case_insensitive=True,  # This is so commands aren't case-sensitive
        )

    async def setup_hook(self) -> None:
        create_database()  # This database setup is blocking and you should be using aiosqlite
        self.remove_command('help')

        for file in sorted(Path("cogs").glob("**/*.py")):
            ext = ".".join(file.parts).removesuffix(".py")
            try:
                await self.load_extension(ext)
                _logger.info("Extension: %s loaded successfully", ext)
            except Exception as error:
                _logger.exception("Extension: %s failed to load\n%s", ext, error)

        _logger.info("Loaded %s cogs!", len(self.cogs))
        _logger.info("\nBot is ready!\nPrefix: %s\nDescription %s", settings.prefix, settings.description)


if __name__ == "__main__":  # Checks if the file is being ran directly
    setup_logging()
    bot = MyBot()
    bot.run(settings.token)
