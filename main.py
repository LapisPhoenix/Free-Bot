# Bot written by: Lapis Pheonix#2194
# Support Me: https://lapispheonix.com
# Want more bots? https://discord.gg/mWSRTKTvMq


from asyncio import sleep
from os import listdir

import discord
from discord.ext import commands

import settings
from database import create_database

bot = commands.Bot(
    command_prefix=settings.prefix, description=settings.description, intents=discord.Intents.all()
)  # Creates the bot, with all intents
bot.remove_command('help')  # Removes the default help command for the custom one


@bot.event
async def on_ready():
    create_database()  # Creates the database if it doesn't exist

    loaded = 0

    for file in listdir('./cogs'):  # Loops through all files in the cogs folder
        if file.endswith('.py'):  # Check if its a python file
            try:
                await bot.load_extension(f'cogs.{file[:-3]}')  # Load the command
            except Exception as e:
                print(f'Failed to load file: {file} with error: {e}')
            else:
                print(f'Loaded File: {file}')  # Print that the command has been loaded
                loaded += 1
    print("Loaded a total of {0} files.".format(loaded))
    await sleep(3)
    print("Bot is ready!\nPrefix: {0}\nDescription: {1}".format(settings.prefix, settings.description))


if __name__ == "__main__":  # Checks if the file is being ran directly
    bot.run(settings.token)
