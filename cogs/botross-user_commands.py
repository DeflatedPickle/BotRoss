from discord.ext import commands


class UserCommands:
    def __init__(self, bot):
        self.bot = bot

        self.help_text = """```          Help:
Command:     Parameters:
paint_image | URL BobType
                                    
URL - The URL of the image you would like to use.
BobType - The image of Bob Ross you would like to use (0 (default), 1, 2, 3, 4 or 5)

Description: Makes the bot paint you a given image.
Example: @BotRoss paint_image https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg 1

help        | None

Description: Sends the bot's help menu.
Example: @BotRoss help

invite      | None

Description: Sends the bot's invite code.
Example: @BotRoss invite```"""

    @commands.command(pass_context=True)
    async def help(self, ctx):
        """Shows the user the commands they can use."""
        self.bot.write_to_log("{} asked for help.".format(ctx.message.author))
        await self.bot.send_message(ctx.message.channel, self.help_text)

    @commands.command(pass_context=True)
    async def invite(self, ctx):
        """Posts the bot's invite link."""
        self.bot.write_to_log("{} asked for the invite code.".format(ctx.message.author))
        await self.bot.send_message(ctx.message.channel, "{}, here's my invite code.".format(ctx.message.author.mention))


def setup(bot):
    bot.add_cog(UserCommands(bot))
