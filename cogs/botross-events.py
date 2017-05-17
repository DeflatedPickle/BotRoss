import discord


class Events:
    def __init__(self, bot):
        self.bot = bot

    async def on_ready(self):
        print("Logging In.")
        await self.update_servers()

    async def on_server_join(self, server):
        await self.update_servers()

    async def on_server_remove(self, server):
        await self.update_servers()

    async def update_servers(self):
        await self.bot.change_presence(game=discord.Game(name="Painting a happy little tree for {} servers.".format(len(self.bot.servers))))


def setup(bot):
    bot.add_cog(Events(bot))
