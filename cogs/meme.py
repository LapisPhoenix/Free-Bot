from requests import get
from random import choice

from discord.ext import commands
from discord import Embed

from settings import Colors

meme_color = Colors.green

class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        reddits = ["funny", "dankmemes", "memes"]   # List of reddits to get memes from
        while True:
            reddit = choice(reddits)
            meme = get(f"https://meme-api.com/gimme/{reddit}").json()   # Get a random meme from the reddit
            if meme['nsfw'] == False:   # Check if the meme is nsfw, if it is, it will loop again
                break
        embed = Embed(title=meme['title'], color=meme_color)
        embed.set_image(url=meme['url'])
        embed.set_footer(text=f"👍 {meme['ups']}")  # Set the footer to the amount of upvotes
        await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(Meme(bot))