from settings import Colors
from discord import Embed
from discord.ext import commands

purge_color = Colors.pink

class Purge(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.has_permissions(manage_messages=True)
    @commands.command()
    async def purge(self, ctx, amount: int = 5):
        #Note: This command is laggy, using this command with large amounts of messages will cause lag because rate limits
        
        if amount > 500:  # Checks if the amount is greater than 500
            return await ctx.send("You can only delete 500 messages at a time.")
        await ctx.channel.purge(limit=amount + 1)  # Deletes messages, default is 5 messages + 1 for the command message
        embed = Embed(title="Purge", description=f"Deleted {amount} messages.", color=purge_color)
        await ctx.send(embed=embed, delete_after=5)  # Sends embed, then deletes it after 5 seconds


async def setup(bot):
    await bot.add_cog(Purge(bot))
