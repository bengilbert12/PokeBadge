from typing import Any, Coroutine
from twitchio.ext import commands
from tinydb import TinyDB, Query

db = TinyDB('db.json')

class StreamerCog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
    
    async def cog_check(self, ctx: commands.Context) -> Coroutine[Any, Any, bool]:
        return ctx.author.name == ctx.channel.name
    
    @commands.command()
    async def levelagain(self, ctx: commands.Context):
        trainer_table = db.table('trainers')
        Trainer = Query()
        trainer_table.upsert({'can_level' : True}, (Trainer['streamer'] == ctx.channel.name))
        await ctx.send(f"{ctx.channel.name}'s viewers can now level again!")

def prepare(bot: commands.Bot):
    bot.add_cog(StreamerCog(bot))
