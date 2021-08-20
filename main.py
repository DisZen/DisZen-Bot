import os
from datetime import datetime

import discord
from discord.ext import commands
from dotenv import load_dotenv


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix=commands.when_mentioned_or('!'),
                         description="DisZen Utility Bot!", )

    async def on_ready(self):
        await bot.change_presence(activity=discord.Activity(name='Shopping DisZen!'))
        print(f'Logged in as {self.user} (ID: {self.user.id}) with time {now}')
        print('------------------')


bot = Bot()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")

load_dotenv()
TOKEN = os.getenv('DISCORD-TOKEN')


@bot.command(name='test')
async def test(ctx):
    await ctx.send("Pinged <@521408201908944907>! :)")


@bot.event
async def on_command_error(ctx, error):
    eri = ctx.message.content
    await ctx.send(content="", embed=discord.Embed(title="Oh no...!",
                                                   url="https://www.youtube.com/watch?v=dQw4w9WgXcQ",
                                                   description=f"The command seems to have crashed!\n"
                                                               f"Something went wrong with `{eri}`",
                                                   color=0xc8142f, timestamp=datetime.utcnow()))
    print({error})


bot.run(TOKEN)
