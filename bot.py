from discord import Intents, Game
from discord.ext.commands import Bot, when_mentioned
from discord_slash import SlashCommand

from config import read_config, write_config, read_id

intents = Intents.default()

bot = Bot(
    command_prefix=when_mentioned,  # command_prefix="!",
    # self_bot=True,
    # help_command=None,
    intents=intents,
)
slash = SlashCommand(
    bot,
    sync_commands=True,
)


@bot.event
async def on_ready():
    print(f"Painting happy little trees for {len(bot.guilds)} guilds")

    config = read_config()

    for i in bot.guilds:
        if i.id not in config:
            config[i.id] = {
            }

    write_config(config)

    await bot.change_presence(activity=Game(name="Painting a happy little tree"))


if __name__ == "__main__":
    from cogs.slash import CogSlash

    bot.add_cog(CogSlash(bot))

    bot.run(read_id())
