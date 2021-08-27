import discord
from discord.ext import commands

import asyncio


class ModerationCog(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="purge", hidden=True)
    @commands.has_permissions(manage_messages=True)
    async def purge(self, ctx, *, amount: int = 5):
        await ctx.channel.purge(limit=amount + 1)
        mess = await ctx.send(embed=discord.Embed(title="Messages purged",
                                                  description=f"Purged **{amount}** messages!",
                                                  color=0x838181))
        await asyncio.sleep(3)
        await mess.delete()


def setup(bot):
    bot.add_cog(ModerationCog(bot))
