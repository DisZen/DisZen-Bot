import asyncio
import traceback
from os import listdir
from os.path import isfile, join

import os
from datetime import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'),
                         description="DisZen Utility Bot!", intents=intents)

    async def on_ready(self):
        bot.loop.create_task(change_status())

        print(f'Logged in as {self.user} (ID: {self.user.id}) with time {now}')
        print('------------------')


intents = discord.Intents.default()
intents.members = True
bot = Bot()

initial_extensions = ['cogs.joinleave',
                      'cogs.owner',
                      'cogs.cmd']

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

load_dotenv()
TOKEN = os.getenv('DISCORD-TOKEN')
cogs_dir = "cogs"


async def change_status():
    while True:
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="the server with **!help**"))
        await asyncio.sleep(10)
        await bot.change_presence(activity=discord.Streaming(name="DisZen Shop", url="https://diszen.com"))


@bot.command(name='test')
async def test(ctx):
    await ctx.send("Pinged <@521408201908944907>! :)")


# @bot.event
# async def on_command_error(ctx, error):
#     eri = ctx.message.content
#     await ctx.send(content="", embed=discord.Embed(title="Oh no...!",
#                                                    url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#                                                    description=f"The command seems to have crashed!\n"
#                                                                f"Something went wrong with `{eri}`",
#                                                    color=0xc8142f, timestamp=datetime.utcnow()))

#     print({error})

if __name__ == '__main__':
    for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
        try:
            bot.load_extension(cogs_dir + "." + extension)
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {extension}.')
            traceback.print_exc()

bot.run(TOKEN, bot=True, reconnect=True)
# client.run(TOKEN)
