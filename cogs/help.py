# All Help commands are in this file

from discord.ext import commands
from settings import Colors, prefix
from discord import Embed

help_color = Colors.green


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group(invoke_without_command=True)  # Creates main command, and allows it to have subcommands
    async def help(self, ctx):
        embed = Embed(title="Help", description=f"Use `{prefix}help <command>` for more info on a command.",
                      color=help_color)
        embed.add_field(name="Moderation",
                        value="`warn`, `rwarn`, `warns`, `mute`, `unmute`, `mutes`, `kick`, `kicks`, `ban`, `unban`, `purge`")
        
        embed.add_field(name="Utility", value="`userinfo`, `botinfo`, `ping`, `adduser`, `addall`, `status`")
        
        embed.add_field(name="Fun", value="`rank`, `leaderboard`, `8ball`, `coinflip`, `rps`, `meme`")

        await ctx.send(embed=embed)

    @help.command()
    async def warn(self, ctx):
        embed = Embed(title="Help - warn", description="Warns a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}warn <user> <reason>`")

        await ctx.send(embed=embed)

    @help.command()
    async def rwarn(self, ctx):
        embed = Embed(title="Help - rwarn", description="Removes a warn from a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}rwarn <user>`")

        await ctx.send(embed=embed)

    @help.command()
    async def warns(self, ctx):
        embed = Embed(title="Help - warns", description="Shows a user's warns.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}warns <user>`")

        await ctx.send(embed=embed)

    @help.command()
    async def mute(self, ctx):
        embed = Embed(title="Help - mute", description="Mutes a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}mute <user>`")

        await ctx.send(embed=embed)

    @help.command()
    async def unmute(self, ctx):
        embed = Embed(title="Help - unmute", description="Unmutes a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}unmute <user>`")

        await ctx.send(embed=embed)

    @help.command()
    async def mutes(self, ctx):
        embed = Embed(title="Help - mutes", description="Shows all mutes an user has had", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}mutes <user>`")

        await ctx.send(embed=embed)

    @help.command()
    async def ping(self, ctx):
        embed = Embed(title="Help - ping", description="Shows the bot's latency.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}ping`")

        await ctx.send(embed=embed)

    @help.command()
    async def kick(self, ctx):
        embed = Embed(title="Help - kick", description="Kicks a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}kick <user> <reason>`")

        await ctx.send(embed=embed)

    @help.command()
    async def ban(self, ctx):
        embed = Embed(title="Help - ban", description="Bans a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}ban <user> <reason>`")

        await ctx.send(embed=embed)

    @help.command()
    async def unban(self, ctx):
        embed = Embed(title="Help - unban", description="Unbans a user.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}unban <user ID>` (Note: it has to be the user ID!)")

        await ctx.send(embed=embed)

    @help.command()
    async def bans(self, ctx):
        embed = Embed(title="Help - bans", description="Shows all bans an user has had", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}bans <user>`")

        await ctx.send(embed=embed)

    @help.command(alias=["ui", "whois"])
    async def userinfo(self, ctx):
        embed = Embed(title="Help - userinfo", description="Shows info about a user.", color=help_color)
        embed.add_field(name="Usage",
                        value=f"`{prefix}userinfo <user>` (Note: if no user is specified, it will show your info)")

        await ctx.send(embed=embed)

    @help.command(aliases=['botf', 'binfo', 'bf'])
    async def botinfo(self, ctx):
        embed = Embed(title="Help - botinfo", description="Shows info about the bot.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}botinfo`")

        await ctx.send(embed=embed)

    @help.command()
    async def purge(self, ctx):
        embed = Embed(title="Help - purge", description="Deletes a specified amount of messages.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}purge <amount>` (Note: Defaults to 5, max is 500)")

        await ctx.send(embed=embed)

    @help.command()
    async def addall(self, ctx):
        embed = Embed(title="Help - addall", description="Adds all users to the database.", color=help_color)
        embed.add_field(name="Usage",
                        value=f"`{prefix}addall` (Note: THIS COMMAND IS EXTEMELY DANGEROUS AND CAN CAUSE A LOT OF ISSUES IF USED INCORRECTLY. ONLY USE WHEN ABSOLUTELY NECESSARY!)")

        await ctx.send(embed=embed)

    @help.command()
    async def adduser(self, ctx):
        embed = Embed(title="Help - adduser", description="Adds a user to the database.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}adduser <user>`")

        await ctx.send(embed=embed)

    @help.command()
    async def leaderboard(self, ctx):
        embed = Embed(title="Help - leaderboard", description="Top 10 users in the server.", color=help_color)
        embed.add_field(name="Usage", value=f"{prefix}leaderboard")

        await ctx.send(embed = embed)
    
    @help.command()
    async def rank(self, ctx):
        embed = Embed(title="Help - rank", description="Shows your own rank and xp.", color=help_color)
        embed.add_field(name="Usage", value=f"{prefix}rank")
        
        await ctx.send(embed = embed)

    @help.command(alias=["8ball"])
    async def eightball(self, ctx):
        embed = Embed(title="Help - 8ball", description="Ask the magic 8ball a question.", color=help_color)
        embed.add_field(name="Usage", value=f"{prefix}8ball <question>")
        
        await ctx.send(embed = embed)
    
    @help.command()
    async def coinflip(self, ctx):
        embed = Embed(title="Help - coinflip", description="Flips a coin.", color=help_color)
        embed.add_field(name="Usage", value=f"{prefix}coinflip")
        
        await ctx.send(embed = embed)
    
    @help.command()
    async def rps(self, ctx):
        embed = Embed(title="Help - rps", description="Play rock paper scissors.", color=help_color)
        embed.add_field(name="Usage", value=f"{prefix}rps <rock/paper/scissors>")
        
        await ctx.send(embed = embed)
    
    @help.command()
    async def kicks(self, ctx):
        embed = Embed(title="Help - kicks", description="Shows all kicks an user has had", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}kicks <user>`")
        
        await ctx.send(embed = embed)

    @help.command()
    async def status(self, ctx):
        embed = Embed(title="Help - status", description="Edits the bot's status.", color=help_color)
        embed.add_field(name="Usage", value=f"`{prefix}status <status>`")
        
        await ctx.send(embed = embed)

async def setup(bot):
    await bot.add_cog(Help(bot))
