from discord.ext import commands
import json

# https://discordapp.com/oauth2/authorize?client_id=313728091702951937&scope=bot&permissions=0

description = "A Discord bot that will make Bob Ross paint a given image."

startup_extentions = ["cogs.botross-admin_commands", "cogs.botross-user_commands", "cogs.botross-paint", "cogs.botross-events"]

bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)
bot.remove_command("help")


def load_credentials():
    with(open(r"credentials.json")) as f:
        return json.load(f)

##################################################

if __name__ == "__main__":
    credentials = load_credentials()
    bot.token = credentials["token"]
    bot.client_id = credentials["client_id"]

    for extention in startup_extentions:
        bot.load_extension(extention)

    bot.run(bot.token)
