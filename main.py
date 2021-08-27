import asyncio
import os
import traceback
from datetime import datetime
from os.path import isfile, join

import discord
from discord.ext import commands
from dotenv import load_dotenv


class Bot(commands.Bot):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if 'prefix' in kwargs.keys():
            self.prefix = kwargs['prefix']
        else:
            self.prefix = None

    async def on_ready(self):
        self.loop.create_task(self.change_status())

        now = str(datetime.now())[:-10]
        print(f'Logged in as {self.user} (ID: {self.user.id}) with time {now}')
        print('------------------')

    async def change_status(self):
        while True:
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,
                                                                name="you 👀."))
            await asyncio.sleep(10)
            await self.change_presence(activity=discord.Streaming(name="DisZen Shop", url="https://diszen.com"))
            await asyncio.sleep(10)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                name="commands."))
            await asyncio.sleep(1)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                name="commands.."))
            await asyncio.sleep(1)
            await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,
                                                                name="commands..."))
            await asyncio.sleep(8)


intents = discord.Intents.default()
intents.members = True
PREFIX = '!'
bot = Bot(command_prefix=commands.when_mentioned_or(PREFIX), description="DisZen Utility Bot!", intents=intents, prefix=PREFIX)


initial_extensions = [
    'cogs.joinleave',
    'cogs.master',
    'cogs.cmd',
    'cogs.errorhandler',
    'cogs.help',
    'cogs.moderation'
]


load_dotenv()
TOKEN = os.getenv('DISCORD-TOKEN')
cogs_dir = 'cogs'

for file in os.listdir(cogs_dir):
    if file.endswith('.py') and isfile(join(cogs_dir, file)):
        file = file[:-3]
        try:
            bot.load_extension(f'{cogs_dir}.{file}')
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {file}.')
            traceback.print_exc()


bot.run(TOKEN, bot=True, reconnect=True)
