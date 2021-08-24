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

    async def on_ready(self):
        self.loop.create_task(self.change_status())

        now = str(datetime.now())[:-10]
        print(f'Logged in as {self.user} (ID: {self.user.id}) with time {now}')
        print('------------------')

    async def change_status(self):
        while True:
            await self.change_presence(
                activity=discord.Activity(type=discord.ActivityType.watching, name="the server with **!help**"))
            await asyncio.sleep(10)
            await self.change_presence(activity=discord.Streaming(name="DisZen Shop", url="https://diszen.com"))
            await asyncio.sleep(10)

    async def on_command_error(self, ctx: commands.context.Context, exception):
        exception = getattr(exception, 'original', exception)

        ignore_exceptions = (commands.CommandNotFound, )

        embed = discord.Embed(colour=discord.Colour.red())

        if type(exception) in ignore_exceptions:
            return

        if isinstance(exception, commands.MissingPermissions):
            print(exception.missing_perms)
            embed.set_author(name="Missing Permissions")
            embed.description = "You don't have the required permissions"

        elif isinstance(exception, commands.MissingRequiredArgument):
            embed.set_author(name="Missing Required Argument")
            embed.description = f"Missing arguments: `<{exception.param.name}>`"
            embed.add_field(name="Correct Usage", value=f"`{PREFIX}{ctx.command} {ctx.command.usage}`")

        elif isinstance(exception, commands.ArgumentParsingError):
            print("Argument Parsing Error")
            embed.description = "Argument Parsing Error"

        elif isinstance(exception, commands.ConversionError):
            embed.description = "Conversion Error"

        elif isinstance(exception, commands.BadArgument):
            if isinstance(exception, commands.MemberNotFound):
                embed.set_author(name="Invalid Member")
                embed.description = f"{exception.argument} is an invalid member"

            elif isinstance(exception, commands.RoleNotFound):
                embed.set_author(name="Invalid Role")
                embed.description = f"{exception.argument} is an invalid role"

            elif isinstance(exception, commands.ChannelNotFound):
                embed.set_author(name="Invalid Channel")
                embed.description = f"{exception.argument} is an invalid channel"

            else:
                print(exception)
                print(exception.__cause__)
                embed.set_author(name="Invalid Argument")
                embed.description = "The argument type is invalid"

        else:
            embed.description = "Oops, an unknown error occurred."
            print(exception)
            print(exception)

        await ctx.send(embed=embed)


intents = discord.Intents.default()
intents.members = True
PREFIX = '!'
bot = Bot(command_prefix=commands.when_mentioned_or(PREFIX), description="DisZen Utility Bot!", intents=intents)


initial_extensions = [
    'cogs.joinleave',
    'cogs.owner',
    'cogs.cmd'
]


load_dotenv()
TOKEN = os.getenv('DISCORD-TOKEN')
cogs_dir = "cogs"


@bot.command(name='test')
async def test(ctx):
    await ctx.send("Pinged <@521408201908944907>! :)")


for file in os.listdir(cogs_dir):
    if file.endswith('.py') and isfile(join(cogs_dir, file)):
        file = file[:-3]
        try:
            bot.load_extension(f'{cogs_dir}.{file}')
        except (discord.ClientException, ModuleNotFoundError):
            print(f'Failed to load extension {file}.')
            traceback.print_exc()


bot.run(TOKEN, bot=True, reconnect=True)
