import random

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
        await bot.change_presence(
            activity=discord.Activity(type=discord.ActivityType.watching, name="the DisZen shop!"))
        print(f'Logged in as {self.user} (ID: {self.user.id}) with time {now}')
        print('------------------')


intents = discord.Intents.default()
intents.members = True
bot = Bot()

initial_extensions = ['cogs.joinleave']

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

load_dotenv()
TOKEN = os.getenv('DISCORD-TOKEN')


# # Welcome Server command
# @client.event
# async def on_member_join(member):
#     # with open("welcome.txt", 'r') as file:
#     #     lines = file.readlines()
#     #     random_line = random.choice(lines)
#     # await client.get_channel(878356697234690079).send(f"{random_line}")
#     # await client.get_channel(878356697234690079).send(f"bingus")
#     channel = client.get_channel(878356697234690079)
#     embed = discord.Embed(title=f"Welcome {member.name}",
#                           description=f"Thanks for joining {member.guild.name}!")  # F-Strings!
#     embed.set_thumbnail(url=member.avatar_url)  # Set the embed's thumbnail to the member's avatar image!
#     await channel.send(embed=embed)

#
# @client.event
# async def on_member_remove(member):
#     await client.get_channel(878356697234690079).send(f"{member.name} has left")


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
    for extension in initial_extensions:
        bot.load_extension(extension)

bot.run(TOKEN, bot=True, reconnect=True)
# client.run(TOKEN)
