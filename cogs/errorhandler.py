import re
from datetime import datetime

import discord
from discord.ext import commands

import main


class ErrorHandler(commands.Cog, name="errorhandler"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.context.Context, exception):
        exception = getattr(exception, 'original', exception)

        ignore_exceptions = ()

        embed = discord.Embed(colour=discord.Colour.red())

        if type(exception) in ignore_exceptions:
            return

        elif isinstance(exception, commands.MissingPermissions):
            print("Missing Perms:" + exception.missing_perms)
            embed.set_author(name="Missing Permissions")
            embed.description = "You don't have the required permissions!"

        elif isinstance(exception, commands.DisabledCommand):
            embed.set_author(name="Disabled Command")
            embed.description = "That command is disabled!"

        elif isinstance(exception, commands.BotMissingPermissions):
            print("Missing Perms:" + exception.missing_perms)
            embed.set_author(name="Missing Permissions")
            embed.description = "I don't have the required permissions!"

        elif isinstance(exception, commands.MissingRole):
            print("Missing Role:" + exception.missing_role)
            embed.set_author(name="Missing Role")
            embed.description = "You don't have the required role!"

        elif isinstance(exception, commands.MissingRequiredArgument):
            embed.set_author(name="Missing Required Argument")
            embed.description = f"Missing arguments: `<{exception.param.name}>`"
            embed.add_field(name="Correct Usage", value=f"`{main.PREFIX}{ctx.command} {ctx.command.usage}`")

        elif isinstance(exception, commands.ArgumentParsingError):
            print("Argument Parsing Error")
            embed.description = "Argument Parsing Error"

        elif isinstance(exception, commands.ConversionError):
            embed.description = "Conversion Error"

        elif isinstance(exception, commands.BadArgument):
            if isinstance(exception, commands.MemberNotFound):
                embed.set_author(name="Invalid Member")
                embed.description = f"{exception.argument} is an invalid member!"

            elif isinstance(exception, commands.RoleNotFound):
                embed.set_author(name="Invalid Role")
                embed.description = f"{exception.argument} is an invalid role!"

            elif isinstance(exception, commands.ChannelNotFound):
                embed.set_author(name="Invalid Channel")
                embed.description = f"{exception.argument} is an invalid channel!"

            else:
                print(exception)
                print(exception.__cause__)
                embed.set_author(name="Invalid Argument")
                embed.description = "The argument type is invalid!"

        else:
            embed.set_author(name=re.sub(r"(\w)([A-Z])", r"\1 \2", type(exception).__name__))
            embed.description = f"```py\n" \
                                f"{str(exception).capitalize()}" \
                                f"```"
            await ctx.send(embed=embed)
            raise exception

        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(ErrorHandler(bot))
