import urllib.request
import urllib.error

from discord.ext import commands
import thejoyofpynting


class Paint:
    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def paint_image(self, ctx, image: str="https://ih0.redbubble.net/image.353370368.9497/flat,800x800,075,f.u1.jpg", bobtype: int=0):
        with open(r"downloaded_image.png", "wb") as download:
            download.write(urllib.request.urlopen(image).read())
            download.close()
        image = thejoyofpynting.paint_a_picture(r"downloaded_image.png", bobtype)
        image.save(r"image.png", "PNG")

        await self.bot.send_file(ctx.message.channel, filename=r"image.png", content="{}, I've painted you a happy little image.".format(ctx.message.author.mention))

    @paint_image.error
    async def paint_image_on_error(self, ctx):
        await self.bot.send_message(ctx.message.channel, "I couldn't paint this happy little image.")

    @commands.command(pass_context=True)
    async def paint_me(self, ctx, bobtype: int=0):
        pass


def setup(bot):
    bot.add_cog(Paint(bot))
