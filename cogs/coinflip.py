from random import choice
from discord.ext import commands


class Coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["cf"])
    async def coinflip(self, ctx):
        bot_options = ["Heads", "Tails"]  # Possible bot choices

        bot_choice = choice(bot_options)  # Get a random choice from the list

        await ctx.reply(bot_choice)  # Reply with the bot choice


async def setup(bot):
    await bot.add_cog(Coinflip(bot))
