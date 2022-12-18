import discord
from discord.ext import commands
from database import get_mutes, add_mute
from settings import Colors, MuteRole, default_mute_time
from asyncio import sleep

mute_color = Colors.purple

class Mute(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mute(self, ctx, member: discord.Member, time_minutes: float = default_mute_time):
        """Mutes a user."""

        time = time_minutes * 60  # Converts seconds to minutes

        if MuteRole.roleId == None:
            return await ctx.author.send("The mute role has not been set.")
        else:
            role = discord.utils.get(ctx.guild.roles, id=MuteRole.roleId)  # Checks for the role in settings.py

        if member.id == ctx.author.id:
            return await ctx.send("You can't mute yourself.")  # Checks if the user is trying to mute themselves
        elif member not in ctx.guild.members:
            return await ctx.send("That user is not in this server.")  # Checks if the user is in the server
        elif member.id == self.bot.user.id:
            return await ctx.send("You can't mute me.")  # Checks if the user is trying to mute the bot

        if role in member.roles:
            return await ctx.author.send(
                "[**ERROR**] That user is already muted.")  # Checks if the user is already muted
        else:
            await member.add_roles(role)  # Adds the mute role to the user if first check passes

            add_mute(member.id)  # DOES NOT ADD ROLE, ONLY ADDS TO DATABASE

            embed = discord.Embed(title=f"Muted {member.name}",
                                  description=f"{member.mention} has been muted for {time_minutes} minute(s).",
                                  color=mute_color)
            embed.add_field(name="Mutes", value=f"New Current Mute Count: `{get_mutes(member.id)}`")

            await ctx.send(f"{member.mention} has been muted.", embed=embed)

            await sleep(time)  # Waits for the time specified

            if role in member.roles:  # Checks if the user is still muted, if they are, it unmutes them, if not, it does nothing

                await member.remove_roles(role)
                embed = discord.Embed(title=f"Unmuted {member.name}", description=f"{member.mention} has been unmuted.",
                                      color=mute_color)

                await ctx.send(f"{member.mention} you have been unmuted.", embed=embed)
            else:
                pass

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def unmute(self, ctx, member: discord.Member):
        """Unmutes a user."""

        if MuteRole.roleId is None:
            return await ctx.author.send("The mute role has not been set.")
        else:
            role = discord.utils.get(ctx.guild.roles,
                                     id=MuteRole.roleId)  # Checks for the role in settings.py, sets it to role

        if member not in ctx.guild.members:
            return await ctx.send("That user is not in this server.")
        elif role not in member.roles:
            return await ctx.author.send("[**ERROR**] That user is not muted.")
        else:
            await member.remove_roles(
                role)  # Same checks as mute command, but now will remove the role if the user is muted

            embed = discord.Embed(title=f"Unmuted {member.name}", description=f"{member.mention} has been unmuted.",
                                  color=mute_color)

            await ctx.send(f"{ctx.author.mention} unmuted {member.mention}.", embed=embed)

    @commands.has_permissions(manage_roles=True)
    @commands.command()
    async def mutes(self, ctx, member: discord.Member):
        """Shows a user's mutes."""

        embed = discord.Embed(title="Current Mutes",
                              description=f"{member.mention} has `{get_mutes(member.id)}` mutes.", color=mute_color)

        await ctx.send(f"{member.mention} mutes.", embed=embed)  # Shows the user's mutes from the database


async def setup(bot):
    await bot.add_cog(Mute(bot))
