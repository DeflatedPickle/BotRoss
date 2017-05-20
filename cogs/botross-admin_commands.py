import discord
from discord.ext import commands

import checks


class AdminCommands:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def change_picture(self, ctx, picture):
        """Change the bot's profile picture."""
        self.bot.write_to_log("{} changed the bot's image.".format(ctx.message.author.name))
        await self.bot.edit_profile(avatar=open(picture, "rb").read())

    @commands.command(pass_context=True)
    @checks.is_owner()
    async def change_game(self, ctx, *, game):
        """Change the bot's game."""
        self.bot.write_to_log("{} changed the bot's game.".format(ctx.message.author.name))
        
        await self.bot.change_presence(game=discord.Game(name=game))

    @commands.command()
    @checks.is_owner()
    async def log_out(self):
        """Logs out the bot."""
        self.bot.write_to_log("Logged out.")
        self.bot.write_to_log("---------------------------------------------------------------------------------------")
        await self.bot.logout()

    @log_out.error
    async def log_out_on_error(self, event, *args, **kwargs):
        await self.bot.say("You must be my owner to log me out.")

    @commands.command()
    @checks.is_owner()
    async def load_cog(self, cog: str):
        """Loads a cog."""
        try:
            self.bot.write_to_log("Loading Cog: {}.".format(cog))
            self.bot.load_extension(cog)
            self.bot.write_to_log("Loaded Cog: {}.".format(cog))
            await self.bot.say("Loaded cog.")
        except ImportError:
            await self.bot.say("That is not a valid cog.")

    @load_cog.error
    async def load_cog_on_error(self, event, *args, **kwargs):
        await self.bot.say("You must be my owner to load a cog.")

    @commands.command()
    @checks.is_owner()
    async def unload_cog(self, cog: str):
        """Unloads a cog."""
        try:
            self.bot.write_to_log("Unloading Cog: {}.".format(cog))
            self.bot.unload_extension(cog)
            self.bot.write_to_log("Unloaded Cog: {}.".format(cog))
            await self.bot.say("Unloaded cog.")
        except ImportError:
            await self.bot.say("That is not a valid cog.")

    @unload_cog.error
    async def unload_cog_on_error(self, event, *args, **kwargs):
        await self.bot.say("You must be my owner to unload a cog.")

    @commands.command()
    @checks.is_owner()
    async def reload_cog(self, cog: str):
        """Reloads a cog."""
        try:
            self.bot.write_to_log("Reloading Cog: {}.".format(cog))
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
            self.bot.write_to_log("Reloaded Cog: {}.".format(cog))
            await self.bot.say("Reloaded cog.")
        except ImportError:
            await self.bot.say("That is not a valid cog.")

    @reload_cog.error
    async def reload_cog_on_error(self, event, *args, **kwargs):
        await self.bot.say("You must be my owner to reload a cog.")


def setup(bot):
    bot.add_cog(AdminCommands(bot))
