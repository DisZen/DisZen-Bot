import discord
from discord.ext import commands


class HelpCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        # self.bot.remove_command("help")

    """
    @commands.command(name="help")
    async def helper(self, ctx, *, arg: str = None):
        embed = discord.Embed()

        if arg is None:
            embed.description = f"Modules - {len(self.bot.cogs)}"
            for mod in self.bot.cogs:
                embed.add_field(name=mod, value=f"`{self.bot.prefix}help {mod}`")
        else:
            mod = arg.lower()
            cogs = self.bot.cogs
            if mod in list(map(lambda s: cogs[s].qualified_name, cogs)):
                for cog in cogs:
                    if mod == cog.lower():
                        for cmd in cogs[cog].get_commands():
                            embed.add_field(name=cmd.name, value=f"{cmd.name}")

                        embed.description = f"Commands - {len(cogs[cog].get_commands())}"
            embed.description = "Oia"

        await ctx.send(embed=embed)
    """


def setup(bot):
    bot.add_cog(HelpCog(bot))
