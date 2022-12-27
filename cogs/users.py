from discord.ext import commands
import discord
from database import add_user, isindatabase
from settings import Colors

user_color = Colors.green


class Users(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def adduser(
        self, ctx, member: discord.Member
    ):  # If for some reason a member didn't get added, you can add them with this command.
        try:
            add_user(member.id, member.name, 0, 0, 0, 0, 0, 1)  # Adds the user to the database.
        except Exception as e:
            return await ctx.send(f"[**ERROR**] User already exists in database.")

        embed = discord.Embed(title="Added User", description=f"Added {member.mention} to the database.", color=user_color)

        await ctx.send(f"{ctx.author.mention} added {member.mention} to the database.", embed=embed)

    @commands.has_permissions(administrator=True)
    @commands.command()
    async def addall(self, ctx):
        # Will attempt to add everyone to the database.
        # THIS COMMAND WILL TAKE A WHILE TO RUN. USE WITH CAUTION.
        # BY USING THIS COMMAND TOO OFTEN, YOU MAY LOCK THE DATABASE.

        guild = ctx.guild  # Gets the guild.

        added = 0

        await ctx.send(
            f"{ctx.author.mention} Adding ***{len(guild.members) - 1}*** users to the database. You will be notified when it is done.\nThis may take a while..."
        )  # -1 to remove the bot from the count.

        for member in guild.members:
            try:
                if member.id == self.bot.user.id:
                    pass
                else:
                    if (
                        isindatabase(member.id) != True
                    ):  # If the user is not in the database, add them. DO NOT REMOVE THIS LINE!!!
                        await ctx.send(f"Adding **{member.name}** to the database.", delete_after=5)
                        add_user(member.id, member.name, 0, 0, 0, 0, 0, 1)
                        added += 1
                    else:
                        await ctx.send(f"**{member.name}** is already in the database.", delete_after=5)
            except Exception as e:
                print(e)

        await ctx.send(
            f"{ctx.author.mention} Added ***{added}*** out of ***{len(guild.members) - 1}*** users to the database."
        )


async def setup(bot):
    await bot.add_cog(Users(bot))
