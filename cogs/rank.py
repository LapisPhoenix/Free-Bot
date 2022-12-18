from discord import Embed
from discord.ext import commands


from database import get_level, get_xp
from settings import Colors

rank_color = Colors.white

class Rank(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @commands.command(aliases=["lvl", "level", "xp", "exp"])
    async def rank(self, ctx):
        #TODO: Add rank card
        
        level = get_level(ctx.author.id)   # Get the level and xp of the user
        xp = get_xp(ctx.author.id)   # Get the level and xp of the user
        embed = Embed(title=f"{ctx.author.name}'s Rank", color=rank_color)
        embed.add_field(name="Xp", value=xp)
        embed.add_field(name="Level", value=level)
        
        try:
            embed.set_thumbnail(url=ctx.author.avatar._url)   # Set the thumbnail to the user's avatar
        except Exception:
            pass
        
        await ctx.send(embed=embed)
        
async def setup(bot):
    await bot.add_cog(Rank(bot))