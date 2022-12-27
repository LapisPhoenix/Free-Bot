from discord import Embed, Member, User
from discord.ext import commands

from database import add_kick, get_kicks
from settings import Colors

kick_color = Colors.orange


class Kick(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: Member, *, reason: str = "No Reason Provided."):

        if member.id == ctx.author.id:
            return await ctx.send("You can't kick yourself.")
        elif member not in ctx.guild.members:
            return await ctx.send("That user is not in this server.")
        elif member.id == self.bot.user.id:
            return await ctx.send(
                "You can't kick me."
            )  # Check if the user is trying to kick themselves, or the bot. And Checks if the user is in the server.

        await member.kick(reason=reason)  # Kicks the user
        add_kick(member.id)  # Adds a kick to the database

        embed = Embed(
            title=f"Kicked {member.name}",
            description=f"{member.mention} has been kicked because {reason}.",
            color=kick_color,
        )

        await ctx.send(embed=embed)

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def kicks(self, ctx, user: User):
        person = await self.bot.fetch_user(
            user.id
        )  # Gets the user object from the id, even if the person isn't in the server.
        embed = Embed(
            title=f"{person.name}'s Kicks", description=f"{person} has `{get_kicks(user.id)}` kicks.", color=kick_color
        )

        await ctx.send(embed=embed)  # Just gets the kicks from the database and sends it in an embed.


async def setup(bot):
    await bot.add_cog(Kick(bot))
