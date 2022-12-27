from database import leaderboard
from settings import Colors

from discord.ext import commands
from discord import Embed

leaderboard_color = Colors.yellow


class Leaderboard(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["leaderboard"])
    async def lb(self, ctx):
        board = leaderboard()  # Get the leaderboard

        embed = Embed(title="Leaderboard", color=leaderboard_color)
        for i in range(
            10
        ):  # Loop through the top 10, if there are less than 10, it will just loop through the amount of people, add people to the embed
            try:
                user = await self.bot.fetch_user(board[i][0])
                embed.add_field(
                    name=f"#{i+1} {user.name}", value=f"Xp: `{board[i][3]}`| Level: `{board[i][2]}`", inline=False
                )  # Add the user to the embed, with their xp and level, and name
            except Exception:
                pass

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Leaderboard(bot))
