from twitchio.ext import commands

class BasicCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    async def cog_check(self, ctx: commands.Context):
        return ctx.message.author.is_mod

    @commands.command()
    async def cogtest(self, ctx: commands.Context):
        await ctx.send("yay it worked")


def prepare(bot: commands.Bot):
    bot.add_cog(BasicCog(bot))
