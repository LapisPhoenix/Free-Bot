# Handles events such as on_member_join, on_command_error, etc.
# If you want to add more events, just add them here.


from database import add_user, add_xp, get_level
from settings import Leveling, Welcome
from discord.ext import commands
from typing import Optional
from discord import Message, Embed


class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._cd = commands.CooldownMapping.from_cooldown(3, 6.0, commands.BucketType.member)

    def get_ratelimit(self, message: Message) -> Optional[int]:
        """Returns the ratelimit left"""
        bucket = self._cd.get_bucket(message)
        return (
            bucket.update_rate_limit()
        )  # Code stolen from https://stackoverflow.com/questions/65940721/cooldown-for-on-message-in-discord-py

    @commands.Cog.listener()
    async def on_member_join(self, member):
        try:
            add_user(member.id, member.name, 0, 0, 0, 0, 0, 1)  # Automatically adds user to database when they join.
        except Exception as e:
            print(e)
        if Welcome.on:
            embed = Embed(
                title=f"Welcome {member.name}!", description=f"Thanks for joining {member.guild.name}!", color=Welcome.color
            )
            embed.set_thumbnail(url=member.avatar._url)
            embed.add_field(name="Remember to read the rules!", value="You can find them in the rules channel.")

            await member.send(embed=embed)  # Sends a welcome message to the user when they join.
        else:
            pass

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.CommandNotFound):
            pass
        elif isinstance(error, commands.MissingRequiredArgument):
            await ctx.send(
                f"[**ERROR**] Missing required argument.\nTry `{ctx.prefix}help {ctx.command}` for more information."
            )
        elif isinstance(error, commands.MissingPermissions):
            await ctx.send(f"[**ERROR**] Missing permissions.")
        elif isinstance(error, commands.BotMissingPermissions):
            await ctx.send(f"[**ERROR**] Bot missing permissions.")
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"[**ERROR**] Command on cooldown.")
        elif isinstance(error, commands.NotOwner):
            await ctx.send(f"[**ERROR**] You are not the owner of this bot.")
        elif isinstance(error, commands.DisabledCommand):
            await ctx.send(f"[**ERROR**] Command is disabled.")
        elif isinstance(error, commands.NoPrivateMessage):
            await ctx.send(f"[**ERROR**] Command cannot be used in private messages.")
        elif isinstance(error, commands.BadArgument):
            await ctx.send(f"[**ERROR**] Bad argument.")
        else:
            if "TypeError: 'NoneType' object is not subscriptable" in str(error):
                await ctx.send(f"[**ERROR**] Invalid user.\nUser not found.")

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.id == self.bot.user.id:  # If the message author is the bot, do nothing
            return
        else:
            ratelimit = self.get_ratelimit(message)  # Checks if the user is ratelimited, cooldown

            if ratelimit is None:  # If the user is not ratelimited, add xp
                try:
                    old_level = get_level(message.author.id)  # Gets the old level of the user
                    add_xp(message.author.id)  # Adds xp to the user
                    new_level = get_level(message.author.id)  # Gets the new level of the user
                    if new_level == old_level + 1:  # If the user leveled up, send a message
                        await message.channel.send(
                            Leveling.LEVEL_UP_MESSAGE.format(user=message.author.mention, level=get_level(message.author.id))
                        )
                    else:
                        pass  # If the user didn't level up, do nothing
                except TypeError:
                    pass
            else:
                pass  # If the user didn't level up, do nothing


async def setup(bot):
    await bot.add_cog(Events(bot))
