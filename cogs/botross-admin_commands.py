import os

import discord
from discord.ext import commands
import checks


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @checks.is_owner()
    async def change_picture(self, picture):
        await self.bot.edit_profile(avatar=open(picture, "rb").read())

    @commands.command()
    @checks.is_owner()
    async def change_game(self, game):
        await self.bot.change_presence(game=discord.Game(name=game))

    @commands.command()
    @checks.is_owner()
    async def log_out(self):
        """Logs out the bot."""
        print("-----------------------------------------------------------------------------------------")
        print("Logging out.")
        await self.bot.logout()

    @log_out.error
    async def log_out_on_error(self, ctx):
        print("-----------------------------------------------------------------------------------------")
        print("{} tried to log out the bot.".format(ctx.message.author))
        await self.bot.say("You must be my owner to log me out.")

    @commands.command(pass_context=True)
    @commands.has_role("Administrator")
    async def say(self, ctx, *, message: str):
        print("-----------------------------------------------------------------------------------------")
        print("{} told bot to say '{}'.".format(ctx.message.author.name, message))
        await self.bot.say(message)

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def say_channel(self, ctx, channel, *, message: str):
        print("-----------------------------------------------------------------------------------------")
        print("{} told bot to say '{}' in {}.".format(ctx.message.author.name, message, channel))
        await self.bot.send_message(self.bot.get_channel(channel), content=message)


def setup(bot):
    bot.add_cog(AdminCommands(bot))
