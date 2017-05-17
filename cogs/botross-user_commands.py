from discord.ext import commands


class UserCommands:
    def __init__(self, bot):
        self.bot = bot

        self.help_text = """```          Help:
Command:     Parameters:
paint_image | URL BobType
                                    
URL - The URL of the image you would like to use.
BobType - The image of Bob Ross you would like to use (0 (default), 1 or 2)
Example: @BotRoss paint_image https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg 1```"""

    @commands.command(pass_context=True)
    async def help(self, ctx):
        await self.bot.send_message(ctx.message.channel, self.help_text)


def setup(bot):
    bot.add_cog(UserCommands(bot))
