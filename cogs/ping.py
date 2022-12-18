from discord.ext import commands


class Ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(
            'Pong!\nLatency: **{0}ms**'.format(round(self.bot.latency * 1000, 1)))  # Sends latency in miliseconds, how long it takes for the bot to respond


async def setup(bot):
    await bot.add_cog(Ping(bot))
