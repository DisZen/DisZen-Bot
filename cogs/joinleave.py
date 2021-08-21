import random
import discord
from discord.ext import commands


class MembersCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def joined(self, ctx, *, member: discord.Member):
        """Says when a member joined."""
        # with open("txt/welcome.txt", 'r') as file:
        #     lines = file.readlines()
        #     random_line = random.choice(lines)
        # await client.get_channel(878356697234690079).send(f"{random_line}")
        # await client.get_channel(878356697234690079).send(f"bingus")
        channel = self.get_channel(878356697234690079)
        embed = discord.Embed(title=f"Welcome {member.name}",
                              description=f"Thanks for joining {member.guild.name}!")  # F-Strings!
        embed.set_thumbnail(url=member.avatar_url)  # Set the embed's thumbnail to the member's avatar image!
        await channel.send(embed=embed)
        # await ctx.send(f'{member.display_name} joined on {member.joined_at}')

    @commands.command(name='coolbot')
    async def cool_bot(self, ctx):
        with open("txt/welcome.txt", 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)
        await ctx.send(random_line)

    @commands.command(name='top_role', aliases=['toprole'])
    @commands.guild_only()
    async def show_toprole(self, ctx, *, member: discord.Member = None):
        """Simple command which shows the members Top Role."""

        if member is None:
            member = ctx.author

        await ctx.send(f'The top role for {member.display_name} is {member.top_role.name}')

    @commands.command(name='perms', aliases=['perms_for', 'permissions'])
    @commands.guild_only()
    async def check_permissions(self, ctx, *, member: discord.Member = None):
        if not member:
            member = ctx.author

        perms = '\n'.join(perm for perm, value in member.guild_permissions if value)

        embed = discord.Embed(title='Permissions for:', description=ctx.guild.name, colour=member.colour)
        embed.set_author(icon_url=member.avatar_url, name=str(member))

        embed.add_field(name='\uFEFF', value=perms.replace('_', ' ').capitalize())

        await ctx.send(content=None, embed=embed)


# The setup fucntion below is neccesarry. Remember we give bot.add_cog() the name of the class in this case MembersCog.
# When we load the cog, we use the name of the file.
def setup(bot):
    bot.add_cog(MembersCog(bot))
