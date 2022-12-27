# Dev tools for the bot
# Do not edit unless you know what you are doing
# Do not edit unless you're updating the bot

from datetime import datetime, timedelta
import math


class Time:
    def epoch(time):
        now = datetime.now()
        later = timedelta(hours=time)
        end_date = now + later

        epoch = end_date.timestamp()

        return int(epoch)


class Xp:
    def calc_xp(
        level: int,
    ):  # The formula used to calculate the xp needed to level up, gotten from https://blog.jakelee.co.uk/converting-levels-into-xp-vice-versa/
        return (level / 0.3) ** 2  # AKA XP = (level/0.3)^2, ask me if you want to change the formula amounts

    def calc_lvl(xp: int):
        return 0.07 * math.sqrt(xp)  # AKA level = 0.07 * √XP

    max_xp: int = 20  # The max amount of xp a user can get from a message
    min_xp: int = 5  # The min amount of xp a user can get from a message
