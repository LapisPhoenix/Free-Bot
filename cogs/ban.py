from discord.ext import commands
from database import add_bans, get_bans
from discord import Embed, Member
from settings import Colors


ban_color = Colors.red


class Ban(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: Member, *, reason: str = "No Reason Provided."):
        if member.id == ctx.author.id:
            return await ctx.send("You can't ban yourself.")
        elif member not in ctx.guild.members:
            return await ctx.send("That user is not in this server.")
        elif member.id == self.bot.user.id:
            return await ctx.send(
                "You can't ban me."
            )  # Check if the user is trying to ban themselves, or the bot. And Checks if the user is in the server.

        add_bans(member.id)  # Add a ban to the database
        await ctx.guild.ban(member, reason=reason)  # Ban the user
        embed = Embed(
            title=f"Banned {member.name}", description=f"{member.mention} has been banned because {reason}.", color=ban_color
        )
        embed.add_field(name="Bans", value=f"New Current Ban Count: `{get_bans(member.id)}`")

        await ctx.send(f"{ctx.author.mention} banned {member}.", embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def unban(self, ctx, userID: int):

        user = await self.bot.fetch_user(userID)  # Get the user from the ID

        if get_bans(user.id) == 0:  # Check the database for bans
            embed = Embed(title=f"{user.name} is not banned", color=ban_color)  # If the user is not banned, send this embed
            return await ctx.send(embed=embed)

        await ctx.guild.unban(user)  # Unban the user

        embed = Embed(title=f"Unbanned {user.name}", color=ban_color)

        await ctx.send(embed=embed)

    @commands.has_permissions(ban_members=True)
    @commands.command()
    async def bans(self, ctx, userID: int):

        user = await self.bot.fetch_user(userID)  # Get the user from the ID

        embed = Embed(description=f"{user} has `{get_bans(user.id)}` bans.", color=ban_color)

        if user.name.endswith("s" or "x" or "z" or "ch" or "sh"):
            embed.title = f"{user.name}' Bans"
        else:
            embed.title = f"{user.name}'s Bans"  # Proper grammar

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Ban(bot))
