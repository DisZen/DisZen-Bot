import asyncio

import discord
from discord.ext import commands


class CmdCog(commands.Cog, name="cmd"):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='repeat', aliases=['copy', 'mimic'], usage="<Your Input>")
    async def do_repeat(self, ctx, *, your_input: str):
        await ctx.send(your_input)

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')

    @commands.command(name='me')
    @commands.is_owner()
    async def only_me(self, ctx):
        await ctx.send(f'Hello {ctx.author.mention}. This command can only be used by you!!')

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is `{member.top_role.name}`')

    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.author

        perms = '\n'.join(perm.capitalize() for perm, value in member.guild_permissions if value).replace('_', ' ')

        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        embed.add_field(name='\uFEFF', value=perms)

        await ctx.send(content=None, embed=embed)

    @commands.command(name='purge', hidden=True)
    @commands.has_role('*')
    async def purge(self, ctx, num: int):
        channel = ctx.channel
        await channel.purge(limit=num+1)
        mess = await ctx.send(embed=discord.Embed(title="Messages purged", description=f"Purged **{num}** messages!",
                                                  color=0x838181))
        await asyncio.sleep(3)
        await mess.delete()

def setup(bot):
    bot.add_cog(CmdCog(bot))
