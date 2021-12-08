import random
from io import BytesIO
from typing import Optional

import requests
from PIL import Image
from discord import File
from discord.ext.commands import Cog, command, Context

from libs.thejoyofpynting import thejoyofpynting

file = "temp/bob.png"
stall = "Hang tight, your masterpiece is coming"


def paint(image, template):
    image_paint = thejoyofpynting.paint_a_picture(
        image,
        template if template != -1 else random.randint(0, 5)
    )
    # Image.open(image_paint).show()
    fi = Image.open(image_paint)
    fi.save(file)


# until we can send images with slash commands, it has to use old style commands
# the class name is a lie :(
class CogSlash(Cog):
    def __init__(self, bot):
        self.bot = bot

    # @cog_slash(
    #     name="paint",
    #     description="Paints the sent image",
    #     options=[
    #         create_option(
    #             name="template",
    #             description="The Bob template to paint your image",
    #             option_type=SlashCommandOptionType.INTEGER,
    #             required=False
    #         ),
    #     ],
    #     guild_ids=read_config(),
    # )
    @command(
        name="paint"
    )
    # TODO: Collect files into a list and send them together?
    async def _paint(self, ctx: Context, template: Optional[int] = -1):
        await self.bot.wait_until_ready()

        if not ctx.message.attachments:
            await ctx.reply("I'm gonna need an attached image, sorry")
        else:
            for f in ctx.message.attachments:
                await ctx.reply(stall)

                bio = BytesIO()
                await f.save(bio)

                paint(bio, template)

                await ctx.reply(
                    file=File(
                        fp=file,
                        filename=f"bob-{f.filename}",
                        spoiler=f.is_spoiler()
                    )
                )

    @command(
        name="paintme"
    )
    async def _paint_me(self, ctx: Context, template: Optional[int] = -1):
        await self.bot.wait_until_ready()

        await ctx.reply(stall)

        bio = BytesIO(requests.get(ctx.message.author.avatar_url).content)

        paint(bio, template)

        await ctx.reply(
            file=File(
                fp=file,
                filename=f"bob-{ctx.message.author.name}.png",
            )
        )
