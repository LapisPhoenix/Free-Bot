from settings import Colors, VERSION, prefix, description
from discord import Embed, __version__ as version_info
from discord.ext import commands

info_color = Colors.green


class Botinfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['botf', 'binfo', 'bf'])
    async def botinfo(self, ctx):
        """Gets general information about the bot."""

        embed = Embed(title="Bot Info", description="Current Status of the bot.", color=info_color)
        embed.add_field(name="Bot Name", value=self.bot.user.name)
        embed.add_field(name="Bot ID", value=self.bot.user.id)
        embed.add_field(name="Bot Prefix", value=prefix)
        embed.add_field(name="Bot Description", value=description if description else "No description set.")
        embed.add_field(name="Commands", value=len(self.bot.commands))
        embed.add_field(name="Bot Version", value=VERSION)
        embed.add_field(name="Bot Creator", value=await self.bot.fetch_user(966515900100538390))  # Gets me as a user object
        embed.add_field(
            name="Nerd Stuff", value="Discordpy version: " + version_info
        )  # Gets the version of discord.py, use this instead of hardcoding it

        embed.set_thumbnail(url=self.bot.user.avatar._url)  # Uses ._url to get the url of the avatar

        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Botinfo(bot))
