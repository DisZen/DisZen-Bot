import discord
import requests
from discord.ext import commands
from discord import Webhook, RequestsWebhookAdapter



class WebHook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.url = "https://discord.com/api/webhooks/880859295858700309/" \
                   "AjDA_MTrUqxd5-j0QqE84ZelBc1mTZSfeE3U5p5efoeesvyElfbgIqxrgMc8t8dBhZbT"

    @commands.command(name="wh", aliases=['webhook', 'hook'], usage="<message>")
    @commands.has_role('*')
    async def webhook(self, ctx, *args):
        if args:
            webhook = Webhook.from_url(self.url, adapter=RequestsWebhookAdapter())
            webhook.send(' '.join(args))
            embed = discord.Embed(colour=discord.Colour.green())
            embed.set_author(name="Success!")
            embed.description = "Sent Webhook message with content:\n" \
                                f"```{' '.join(args)}```\n"
            await ctx.send(embed=embed)
        else:
            embed = discord.Embed(colour=discord.Colour.red())
            embed.set_author(name="Missing Required Argument")
            embed.description = f"Missing arguments: `<message>`"
            embed.add_field(name="Correct Usage", value=f"`!webhook <message>`")


def setup(bot):
    bot.add_cog(WebHook(bot))
