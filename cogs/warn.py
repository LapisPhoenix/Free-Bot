from asyncio import sleep

import discord
from discord.ext import commands

from database import add_bans, add_mute, add_warn, get_mutes, get_warns, remove_warn
from settings import Colors, MuteRole, max_warns_ban, max_warns_mute

warn_color = Colors.red


class Warn(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def warn(self, ctx, member: discord.Member, *, reason: str = "No reason provided."):
        """Warns a user."""

        if member.id == ctx.author.id:
            return await ctx.send("You can't warn yourself.")
        elif member not in ctx.guild.members:
            return await ctx.send("That user is not in this server.")
        elif member.id == self.bot.user.id:
            return await ctx.send(
                "You can't warn me."
            )  # Check if its the author, a member not in the server, or the bot who is trying to be warned...

        add_warn(member.id)

        embed = discord.Embed(
            title=f"Warned {member.name}", description=f"{member.mention} has been warned.", color=warn_color
        )
        embed.add_field(name="Reason", value=reason)
        embed.add_field(name="Warnings", value=f"Total warnings: `{get_warns(member.id)}`")

        await ctx.send(f"{member.mention} has been warned.", embed=embed)

        if get_warns(member.id) == max_warns_ban:  # If the user has reached the max amount of warnings, ban them.
            add_bans(member.id)
            await member.ban(reason="Max warns reached.")
            await ctx.send(f"{member.mention} has been banned for reaching {max_warns_ban} warnings.")

        elif get_warns(member.id) == max_warns_mute:  # If the user has reached the max amount of warnings, mute them.

            if MuteRole.roleId == None:

                return await ctx.author.send(
                    f"**{member.name}** has reached **{max_warns_mute}** warnings, but there is no mute role set!"
                )

            else:

                role = discord.utils.get(ctx.guild.roles, id=MuteRole.roleId)  # Checks for the role in settings.py
                add_mute(member.id)

                await member.add_roles(role)  # Adds the mute role to the user

                embed = discord.Embed(
                    title=f"Muted {member.name}",
                    description=f"{member.mention} has been muted for 60 minute(s).",
                    color=warn_color,
                )

                embed.add_field(name="Mutes", value=f"New Current Mute Count: `{get_mutes(member.id)}`")
                await ctx.send(f"{member.mention} has been muted.", embed=embed)

                await sleep(3600)  # Waits for 1 hour (60 * 60)

                if (
                    role in member.roles
                ):  # Checks if the user is still muted, if they are, it unmutes them, if not, it does nothing
                    await member.remove_roles(role)
                    embed = discord.Embed(
                        title=f"Unmuted {member.name}", description=f"{member.mention} has been unmuted.", color=warn_color
                    )
                    await ctx.send(f"{member.mention} you have been unmuted.", embed=embed)
                else:
                    pass

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def rwarn(self, ctx, member: discord.Member):
        """Removes a warn from a user."""

        if get_warns(member.id) == 0:  # If the user has no warnings, return this message.
            return await ctx.send(f"{member.mention} has no warnings...")
        else:
            remove_warn(member.id)

            embed = discord.Embed(
                title=f"Removed Warning from {member.name}",
                description=f"{member.mention} has had a warning removed.",
                color=warn_color,
            )
            embed.add_field(name="Warnings", value=f"Total warnings: `{get_warns(member.id)}`")

            await ctx.send(f"{member.mention} has had a warning removed.", embed=embed)

    @commands.has_permissions(kick_members=True)
    @commands.command()
    async def warns(self, ctx, member: discord.Member):
        """Shows a user's warns."""

        embed = discord.Embed(
            title=f"Current Warnings - {member.name}",
            description=f"{member.mention} has `{get_warns(member.id)}` total warnings.",
            color=warn_color,
        )

        await ctx.send(f"{member.mention} warnings.", embed=embed)


async def setup(bot):
    await bot.add_cog(Warn(bot))
