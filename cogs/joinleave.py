import random

import discord
from discord.ext import commands


class MembersCog(commands.Cog, name="joinleave"):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        with open("data/welcome.data", 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)

        channel = self.bot.get_channel(878356697234690079)
        embed = discord.Embed(title=f"{member.name} joined!",
                              description=random_line,
                              color=0x94A1B9)
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        with open("data/bye.data", 'r') as file:
            lines = file.readlines()
            random_line = random.choice(lines)

        channel = self.bot.get_channel(878356697234690079)
        embed = discord.Embed(title=f"{member.name} left!",
                              description=random_line,
                              color=0x101c34)
        embed.set_thumbnail(url=member.avatar_url)
        await channel.send(embed=embed)


def setup(bot):
    bot.add_cog(MembersCog(bot))
