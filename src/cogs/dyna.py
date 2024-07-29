from typing import Any, Coroutine
from twitchio.ext import commands
import random
from utils import *


phrases = ['Watch out\'m gonna pep!', "One small pep for man, one giant pep for mankind", 'Would you rather goon or edge?', 'certified mewer', 'certified pepper', 'its all skibidi my little rizzler', 'pep YOU, pep YOU, pep EVERYONE', 'chill im gonna pep my pants', 'im here to pep and pep, and im all out of gum..']

emotes = ['Brows', 'Dance', 'Taps', 'Flip', 'Haw', 'Super', 'Jam', 'Roll', 'Moo', 'Duh', 'Huh', 'Coffee', 'Notes', 'Oof', 'Pls', 'Dumpy', 'Dumpy2', 'Lurk', 'Nod', 'Flower', 'Love', 'Wave', 'Dyna', 'Raid', 'Tourney', 'Sip', 'Sad', 'Stare', 'Lul', 'Pogg', 'Angry', 'Kissy', "Pride", 'Smirk', 'Bedge', 'PEPW', 'Sit', 'Surprise', 'Despair']


class DynaCog(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    async def cog_check(self, ctx: commands.Context) -> Coroutine[Any, Any, bool]:
        return ctx.channel.name in ['dynamungo', 'professorjolteon', 'livekezin','jholl0','benyonce12']
    
    @commands.command()
    async def pep(self, ctx: commands.Context):
        await ctx.send(f"pep yourself {ctx.author.name} *copyright Phizzbot")

    @commands.command()
    async def pepify(self, ctx: commands.Context, *args):
        if not args:
            await ctx.send('Nothing to pep')
        phrase = list(args)
        for index, word in enumerate(phrase):
            if len(word) <= 3:
                phrase[index] = 'pep'
        new = ' '.join(phrase)
        await ctx.send(new)

    @commands.command()
    async def raid(self, ctx: commands.Context):
        await ctx.send("dynamu1Raid  THIS dynamu1Dumpy")

    @commands.command()
    async def pepfuture(self, ctx: commands.Context):
        ran = random.randint(1,2)
        if ran == 1:
            await ctx.send('The future is looking pep(in a bad way)')
        elif ran == 2:
            await ctx.send('The future is looking pep(in a good way)')

    @commands.command()
    async def dynapep(self, ctx: commands.Context):
        await ctx.send(random.choice(phrases))


    @commands.command()
    async def words(self, ctx: commands.Context):
        await ctx.send('Did you try pep?')

    @commands.command()
    async def epilogue(self, ctx: commands.Context):
        await ctx.send('Do you like the cut of Dyna\'s pep? Check out the rest of Epilogue gaming at https://discord.com/invite/epiloguegaming')

    @commands.command()
    async def hawktuah(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} needs someone to spit on that thang!')

    @commands.command()
    async def check(self, ctx: commands.Context):
        if ctx.author.is_subscriber:
            await ctx.send(f'The numbers dont lie. {ctx.author.name} is pep!')
        else:
            await ctx.send(f'Sorry {ctx.author.name}, you are not pep. Maybe try subscribing?')

    @commands.command()
    async def pokecatch(self, ctx: commands.Context):
        await ctx.send(f'{ctx.author.name} wrong bot dummy')

    @commands.command()
    async def rules(self, ctx: commands.Context):
        await ctx.send('no lmao')

    @commands.command()
    async def emote(self, ctx: commands.Context):
        emot = random.choice(emotes)
        await ctx.send(f'dynamu1{emot} dynamu1{emot} dynamu1{emot} dynamu1{emot}')

    @commands.command()
    async def son(self, ctx: commands.Context):
        await ctx.send('Yes daddy dearest? uwu')

    @commands.command()
    async def combo(self, ctx: commands.Context, *args):
        if len(args) != 3:
            await ctx.send('I need three words to combo')
        await ctx.send(f'She {args[0]} on my {args[1]} until I {args[2]}')

    @commands.command()
    async def skibidi(self, ctx: commands.Context):
        trainer = get_trainer(ctx.channel.name, ctx.author.name)
        await ctx.send(f"OH NO! The Rizzler found {trainer['name']}'s {trainer['pokemon']} and griddied all over it! Now {trainer['pokemon']} has Pokerus. NOT SIGMA")




def prepare(bot: commands.Bot):
    bot.add_cog(DynaCog(bot))