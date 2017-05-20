import json
from datetime import datetime


from discord.ext import commands

# https://discordapp.com/oauth2/authorize?client_id=313728091702951937&scope=bot&permissions=0

description = "A Discord bot that will make Bob Ross paint a given image."

startup_extentions = ["cogs.botross-admin_commands", "cogs.botross-user_commands", "cogs.botross-paint", "cogs.botross-events"]

bot = commands.Bot(command_prefix=commands.when_mentioned, description=description)
bot.log_file = "/home/DeflatedPickle/BotRoss/log.txt"
bot.credentials = "/home/DeflatedPickle/BotRoss/credentials.json"
bot.remove_command("help")


def write_to_log(text: str="", also_time=True, also_print=True):
    if also_time:
        time = datetime.now().strftime("%H:%M:%S")
    with open(bot.log_file, "a") as log:
        log.write("{} {}\n".format(str(time) + " |" if also_time else None + " |", text))
        log.close()
        if also_print:
            print("{} {}".format(str(time) + " |" if also_time else None + " |", text))

bot.write_to_log = write_to_log


def load_credentials():
    with(open(bot.credentials)) as creds:
        return json.load(creds)

##################################################

if __name__ == "__main__":
    credentials = load_credentials()
    bot.token = credentials["token"]
    bot.client_id = credentials["client_id"]

    for extention in startup_extentions:
        bot.load_extension(extention)

    bot.run(bot.token)
