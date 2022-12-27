from discord.ext import commands
from discord import Game


class Status(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()  # Checks if the user is the owner of the bot
    @commands.command()
    async def status(self, ctx, *, status):
        await self.bot.change_presence(activity=Game(status))  # Changes the bots status
        await ctx.send(f"Status changed to **{status}**")


async def setup(bot):
    await bot.add_cog(Status(bot))
