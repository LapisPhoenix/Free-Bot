import random

import aiohttp
from discord import Embed
from discord.ext import commands

from settings import Colors


class Meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    async def _get_meme_post(self):
        sub_reddit = random.choice(["funny", "dankmemes", "memes"])
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://www.reddit.com/r/{sub_reddit}.json?limit=15") as data:
                data = await data.json()
                children = data["data"]["children"]

                valid_memes = [
                    item
                    for item in children
                    if not item["data"]["pinned"]
                    if not item["data"]["stickied"]
                    if not item["data"]["over_18"]
                    if item["data"]["post_hint"] == "image"
                ]

                post = random.choice(valid_memes)
                return post

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def meme(self, ctx):
        post = await self._get_meme_post()

        title = post["data"]["title"]
        subreddit = post["data"]["subreddit"]
        upvotes = post["data"]["ups"]
        content_url = post["data"]["url_overridden_by_dest"]

        embed = Embed(title=title, color=Colors.green)
        embed.set_image(url=content_url)
        embed.set_footer(text=f"\U0001f44d {upvotes} | {subreddit}")
        await ctx.send(embed=embed)


async def setup(bot):
    await bot.add_cog(Meme(bot))
