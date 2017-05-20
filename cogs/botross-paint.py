import urllib.request
import urllib.error

from discord.ext import commands
import thejoyofpynting


class Paint:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def paint_image(self, ctx, image: str="https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg", bobtype: int=0):
        """Makes the bot paint a given image."""
        with open("/home/DeflatedPickle/BotRoss/downloaded_image.png", "wb") as download:
            try:
                download.write(urllib.request.urlopen(image).read())
            except urllib.error.HTTPError as error:
                if error.code == 403:
                    await self.bot.say("I could not access this happy little site.")
                    return

                elif error.code == 404:
                    await self.bot.say("This happy little site does not exist.")
                    return
                else:
                    print(error)
                    await self.bot.say("I couldn't paint this happy little image.")
                    return
            download.close()

        image_paint = thejoyofpynting.paint_a_picture("/home/DeflatedPickle/BotRoss/downloaded_image.png", bobtype)
        image_paint.save("/home/DeflatedPickle/BotRoss/painted_image.png", "PNG")

        await self.bot.send_file(ctx.message.channel, fp="/home/DeflatedPickle/BotRoss/painted_image.png", content="{}, I've painted you this happy little image.".format(ctx.message.author.mention))
        self.bot.write_to_log("Painted the file {} for {}.".format(image, ctx.message.author))

    @commands.command(pass_context=True)
    async def paint_me(self, ctx, bobtype: int=0):
        pass


def setup(bot):
    bot.add_cog(Paint(bot))
