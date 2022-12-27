# This file is used to store all the settings for the bot
# Feel free to change, but make sure to keep the same format

# To change a command color, go into the cogs folder and find the file for the command you want to change
# Then change the color variable to the color you want

from typing import Optional

token: str = ""  # The token for the bot, this is required to run the bot
prefix: str = "?"  # Changing this will automatically update for help command
VERSION: str = "1.0.0"  # Current Version of the bot, this is used for the botinfo command
description: str = ""  # The description of the bot, this doesn't show up, but can be used for other things
database_name: str = "user_database.db"  # The name of the database file, spaces will be replaced with underscores
max_warns_mute: int = 3  # The max amount of warns a user can have before they are muted
max_warns_ban: int = (
    5  # The max amount of warns a user can have before they are banned, set to "None" to disable   (THIS WILL INSTANTLY BAN)
)
default_mute_time: int = 60  # The default time a user is muted for in minutes


class Leveling:  # Leveling settings
    # Reccomended to leave max_xp and min_xp at 100 and 5
    # If you do change them, make sure to keep whole numbers

    # Use {user} and {level} in the message to show the user and level they leveled up to
    LEVEL_UP_MESSAGE: str = (
        "Congrats **{user}** you leveled up to level **{level}**!"  # The message sent when a user levels up
    )
    min_xp = 5  # The min amount of xp a user can get from a message
    max_xp = 20  # The max amount of xp a user can get from a message


class Colors:  # Colors for embeds

    # Use this website to get the hex code for the color you want: https://www.color-hex.com/ remove # replace with 0x like below
    # Example: #FF0000 = 0xFF0000
    # To use change the color for the command, enter the command file and edit the color variable

    red = 0xFF0000
    green = 0x00FF00
    blue = 0x0000FF
    yellow = 0xFFFF00
    orange = 0xFFA500
    purple = 0x800080
    pink = 0xFFC0CB
    white = 0xFFFFFF
    black = 0x000000


class MuteRole:
    roleId: Optional[int] = None  # If you do not add a role ID, the command will not work.


class Welcome:
    on = True  # If you want to disable the welcome message, set this to False
    color = Colors.green  # The color of the welcome message
