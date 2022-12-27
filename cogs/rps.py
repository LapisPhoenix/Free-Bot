import random

from discord.ext import commands


class Rockpaperscissors(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=["rps"])
    async def rockpaperscissors(self, ctx, *, choice=None):
        # Command slightly broken, works fine enough for now
        # Will fix in V 2.0

        if choice is None:
            await ctx.send("Please provide a choice.")
        else:
            bot_options = ["Rock", "Paper", "Scissors"]
            bot_choice = random.choice(bot_options)

            if choice == bot_choice:
                await ctx.send(f"*It's a tie!*\nYou chose **{choice}** and I chose **{bot_choice}**.")

            elif choice == "Rock" or "rock" and bot_choice == "Paper":
                await ctx.send(
                    f"*I win!*\nYou chose **{choice}** and I chose **{bot_choice}**\n{bot_choice} covers {choice}."
                )

            elif choice == "Rock" or "rock" and bot_choice == "Scissors":
                await ctx.send(
                    f"*You win!*\nYou chose **{choice}** and I chose **{bot_choice}**.\n{choice} crushes {bot_choice}."
                )

            elif choice == "Paper" or "paper" and bot_choice == "Rock":
                await ctx.send(
                    f"*You win!*\nYou chose **{choice}** and I chose **{bot_choice}**.\n{choice} covers {bot_choice}."
                )

            elif choice == "Paper" or "paper" and bot_choice == "Scissors":
                await ctx.send(
                    f"*I win!*\nYou chose **{choice}** and I chose **{bot_choice}**.\n{bot_choice} cuts {choice}."
                )

            elif choice == "Scissors" or "scissors" and bot_choice == "Rock":
                await ctx.send(
                    f"*I win!*\nYou chose **{choice}** and I chose **{bot_choice}**.\n{bot_choice} crushes {choice}."
                )

            elif choice == "Scissors" or "scissors" and bot_choice == "Paper":
                await ctx.send(
                    f"*You win!*\nYou chose **{choice}** and I chose **{bot_choice}**.\n{choice} cuts {bot_choice}."
                )

            else:
                await ctx.send(
                    f"*I win!*\nYou chose **{choice}** and I chose **{bot_choice}**.\n{bot_choice} beats {choice}."
                )


async def setup(bot):
    await bot.add_cog(Rockpaperscissors(bot))
