from discord import Embed, Member
from discord.ext import commands

from settings import Colors

userinfo_color = Colors.orange


class Userinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['ui', 'whois'])
    async def userinfo(self, ctx, member: Member = None):
        if member is None:
            member = ctx.author  # Checks if a member was passed, if not, it will use the author

        mem_name = member.name  # Gets the member's name
        mem_id = member.id  # Gets the member's ID
        try:
            mem_avatar = member.avatar._url  # Gets the member's avatar
        except Exception:
            pass
        mem_created = member.created_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"
        )  # Gets the member's account creation date in a readable format
        mem_joined = member.joined_at.strftime(
            "%a, %#d %B %Y, %I:%M %p UTC"
        )  # Gets the member's join date in a readable format
        mem_roles = [role.mention for role in member.roles]  # Gets the member's roles, and puts them in a list

        embed = Embed(title=f"{mem_name} ({mem_id})", color=userinfo_color)
        embed.add_field(name="Created At", value=mem_created)
        embed.add_field(name="Joined At", value=mem_joined)
        embed.add_field(name="Roles", value=" ".join(mem_roles), inline=False)

        embed.set_footer(text=f"Requested by {ctx.author}")
        try:
            embed.set_thumbnail(url=mem_avatar)
        except Exception:
            pass

        await ctx.send(f"{ctx.author.mention}", embed=embed)


async def setup(bot):
    await bot.add_cog(Userinfo(bot))
