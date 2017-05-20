import discord


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        self.bot.write_to_log("Logged In.")
        await self.update_servers()

    async def on_server_join(self, server):
        self.bot.write_to_log("Joined the server: {}.".format(server.name))
        await self.update_servers()

    async def on_server_remove(self, server):
        self.bot.write_to_log("Left the server: {}.".format(server.name))
        await self.update_servers()

    async def update_servers(self):
        await self.bot.change_presence(game=discord.Game(name="Painting a happy little tree for {} servers.".format(len(self.bot.servers))))

    async def on_command_error(self, error, ctx):
        if hasattr(ctx.command, "on_error"):
            return

        await self.bot.send_message(ctx.message.channel, "That's not a valid happy little command.")


def setup(bot):
    bot.add_cog(Events(bot))
