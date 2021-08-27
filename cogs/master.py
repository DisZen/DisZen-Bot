import os

from discord.ext import commands
import discord
import inspect


class MasterCog(commands.Cog, name="master"):

    def __init__(self, bot):
        self.bot = bot
        self.cogs_dir = "cogs"

    @commands.command(name='load', hidden=True, usage="<cog>")
    @commands.has_role('*')
    async def load_cog(self, ctx, *, cog: str):
        try:
            self.bot.load_extension(f'{self.cogs_dir}.{cog}')
        except Exception as e:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=f"{type(e).__name__}")
            embed.description = f"{e}"
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name="Success!")
            embed.description = f"Successfully reloaded {cog}!"
            await ctx.send(embed=embed)

    @commands.command(name='unload', hidden=True, usage="<cog>")
    @commands.has_role('*')
    async def unload_cog(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(f'{self.cogs_dir}.{cog}')
        except Exception as e:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=f"{type(e).__name__}")
            embed.description = f"{e}"
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name="Success!")
            embed.description = f"Successfully reloaded {cog}!"
            await ctx.send(embed=embed)

    @commands.command(name='reload', hidden=True, usage="<cog>")
    @commands.has_role('*')
    async def reload_cog(self, ctx, *, cog: str):
        try:
            self.bot.unload_extension(f'{self.cogs_dir}.{cog}')
            self.bot.load_extension(f'{self.cogs_dir}.{cog}')
        except Exception as e:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=f"{type(e).__name__}")
            embed.description = f"{e}"
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name="Success!")
            embed.description = f"Successfully reloaded {cog}!"
            await ctx.send(embed=embed)

    @commands.command(name='listcogs', hidden=True)
    @commands.has_role('*')
    async def list_cogs(self, ctx):
        cogs = self.bot.cogs
        cog_names = '\n- '.join(NameOfCog for NameOfCog, TheClassOfCog in cogs.items())

        embed = discord.Embed(title='', description=f'There are **{len(cogs)}** cogs', colour=ctx.author.colour)
        embed.set_author(icon_url=self.bot.user.avatar_url, name=ctx.guild.name)

        embed.add_field(name='\uFEFF', value=f'- {cog_names}')
        await ctx.send(embed=embed)

    @commands.command(pass_context=True, hidden=True)
    @commands.has_role('*')
    async def debug(self, ctx, *, code: str):
        """Evaluates code."""
        code = code.strip('` ')
        python = '```py\n{}\n```'

        env = {
            'bot': self.bot,
            'ctx': ctx,
            'message': ctx.message,
            'server': ctx.message.guild,
            'channel': ctx.message.channel,
            'author': ctx.message.author
        }

        env.update(globals())

        try:
            result = eval(code, env)
            if inspect.isawaitable(result):
                result = await result
        except Exception as e:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name=type(e).__name__)
            embed.description = python.format(str(e))
            await ctx.send(embed=embed)
            return

        embed = discord.Embed(colour=0x00101c34)
        embed.set_author(name="Code:")
        embed.description = python.format(result)
        await ctx.send(embed=embed)

    @commands.command(name='stop', hidden=True)
    @commands.has_role('*')
    async def stop(self, ctx):
        try:
            embed = discord.Embed(colour=0x00101c34)
            embed.description = "Closing bot!"
            await ctx.send(embed=embed)
            await self.bot.close()
        except:
            embed = discord.Embed(colour=0x00101c34)
            embed.description = "Error!"
            await ctx.send(embed=embed)
            pass

    @commands.command(name='clean', hidden=True)
    @commands.has_role('*')
    async def clean(self, ctx):
        try:
            embed = discord.Embed(colour=0x00101c34)
            embed.description = "Cleaning bot!"
            await ctx.send(embed=embed)
            await self.bot.clear()
        except:
            embed = discord.Embed(colour=0x00101c34)
            embed.description = "Error!"
            await ctx.send(embed=embed)
            pass


def setup(bot):
    bot.add_cog(MasterCog(bot))
