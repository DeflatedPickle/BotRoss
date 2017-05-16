import discord
from discord.ext import commands
import json

# https://discordapp.com/oauth2/authorize?client_id=259489359559000065&scope=bot&permissions=0

description = "A Discord bot that will make Bob Ross paint a given image."

startup_extentions = ["cogs.botross-admin_commands", "cogs.botross-paint"]

bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Logging In.")
    await bot.change_presence(game=discord.Game(name="Painting a happy little tree for {} servers.".format(len(bot.servers))))


# @bot.event
# async def on_command_error(error, ctx):
#     if hasattr(ctx.command, "on_error"):
#         return
#
#     await bot.send_message(ctx.message.channel, error)

##################################################


def load_credentials():
    with(open("credentials.json")) as f:
        return json.load(f)

##################################################

if __name__ == "__main__":
    credentials = load_credentials()
    bot.token = credentials["token"]
    bot.client_id = credentials["client_id"]

    for extention in startup_extentions:
        bot.load_extension(extention)

    bot.run(bot.token)
