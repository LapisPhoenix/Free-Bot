from random import choice

from discord.ext import commands


class Eightball(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["8ball"])
    async def eightball(self, ctx, *, question: str = None):  # question does nothing, but it is required
        if question is None:
            return await ctx.send("Please provide a question.")
        else:
            bot_options = [
                "🟢 It is certain.",
                "🟢 Without a doubt.",
                "🟢 Yes definitely.",
                "🟡 Better not tell you now.",
                "🟡 Cannot predict now.",
                "🟡 Concentrate and ask again.",
                "🔴 Don't count on it.",
                "🔴 My sources say no.",
                "🔴 Very doubtful.",
            ]  # Possible bot choices

            bot_choice = choice(bot_options)  # Get a random choice from the list

            await ctx.reply(bot_choice)  # Reply with the bot choice


async def setup(bot):
    await bot.add_cog(Eightball(bot))
