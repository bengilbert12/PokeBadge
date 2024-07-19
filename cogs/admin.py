from twitchio.ext import commands

class AdminCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    async def cog_check(self, ctx: commands.Context):
        return ctx.message.author.name == "benyonce12"

    @commands.command()
    async def unload(self, ctx: commands.Context, *, module):
        try:
            module = f"cogs.{module}"
            self.bot.unload_module(module)
        except Exception as e:
            print(f"Unloading cog error: {e}")
            await ctx.send(f"Error unloading cog {module}, check logs")

        else:
            await ctx.send(f"Unloaded '{module}'")
            print(f"Unloaded '{module}'")

    @commands.command()
    async def load(self, ctx, *, module):
        try:
            module = f"cogs.{module}"
            self.bot.load_module(module)
        except Exception as e:
            print(f"Loading cog error: {e}")
            await ctx.send(f"Error loading cog {module}, check logs")

        else:
            await ctx.send(f"Loaded '{module}'")
            print(f"Loaded '{module}'")


    @commands.command()
    async def reload(self, ctx, *, module):
        try:
            module = f"cogs.{module}"
            self.bot.unload_module(module)
            self.bot.load_module(module)
        except Exception as e:
            print(f"Reloading cog error: {e}")
            await ctx.send(f"Error reloading cog {module}, check logs")
        else:
            await ctx.send(f"Reloaded '{module}'")
            print(f"Reloaded '{module}'")

def prepare(bot: commands.Bot):
    bot.add_cog(AdminCog(bot))
