from typing import Any, Coroutine
from twitchio.ext import commands

class CobCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    async def cog_check(self, ctx: commands.Context) -> Coroutine[Any, Any, bool]:
        return ctx.channel.name == 'grandpacob'
    
    @commands.command()
    async def youtube(self, ctx: commands.Context):
        await ctx.send('https://www.youtube.com/channel/UCrCjubhYtPY4LttRgtmW4aQ')

    @commands.command()
    async def tiktok(self, ctx: commands.Context):
        await ctx.send('https://www.tiktok.com/@cobstop?lang=en')

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send('https://discord.gg/2xQ6NVXCX2')


def prepare(bot: commands.Bot):
    bot.add_cog(CobCog(bot))