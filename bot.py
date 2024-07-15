import os
from twitchio.ext import commands
from dotenv import load_dotenv
from utils import create_poke, get_poke, get_trainer, level_up_poke


load_dotenv()

TOKEN = os.getenv("TOKEN")
INITIAL_CHANNELS = os.getenv("INITIAL_CHANNELS").split(',')
print(INITIAL_CHANNELS)


DISCORD_INVITE=os.getenv('DISCORD_INVITE')

class Bot(commands.Bot):

    def __init__(self):
        super().__init__(token=TOKEN, prefix='?', initial_channels=INITIAL_CHANNELS)

    async def event_ready(self):
        print(f'Logged in as | {self.nick}')
        print(f'User id is | {self.user_id}')

    async def event_message(self, message):
        if message.echo:
            return
        print(message.content)
        await self.handle_commands(message)
    
    @commands.command()
    async def hello(self, ctx: commands.Context):
        await ctx.send(f'Hello {ctx.author.name}!')

    @commands.command()
    async def discord(self, ctx: commands.Context):
        await ctx.send(f"Join our Discord at {DISCORD_INVITE}")

    @commands.command()
    async def dance(self, ctx: commands.Context):
        if not ctx.channel.name == "grandpacob":
            await ctx.send("sumcorSHINYSPROUT sumcorSHINYSPROUT sumcorSHINYSPROUT sumcorSHINYSPROUT")

    @commands.command(aliases = ['pepmon'])
    async def pokegen(self, ctx: commands.Context):
        # if not ctx.message.author.is_subscriber:
        #     await ctx.send("Only subscribers can generate Pokemon")
        #     return
        poke = get_poke(ctx.channel.name, ctx.author.name)
        if not poke:
            poke = create_poke(ctx.channel.name, ctx.author.name)
            await ctx.send(f"{ctx.author.name}'s random Pokemon is {poke}!")
            return
        await ctx.send(f"{ctx.author.name} already generated a {poke}")

    @commands.command()
    async def schedule(self, ctx: commands.Context):
        if not ctx.channel.name == "grandpacob":
            await ctx.send("Cob usually streams all days except Mondays and Fridays starting at 11AM EST")

    @commands.command()
    async def suggest(self, ctx: commands.Context, suggestion):
        sug = open("suggestions.txt","a")
        sug.write(f"{suggestion}")
        sug.close()
        await ctx.send(f"Thanks for the suggestion, {ctx.author.name}. It has been logged and will be reviewed!")

    @commands.command()
    async def barry(self, ctx: commands.Context):
        await ctx.send("Barry is a big ol bitch")

    @commands.command()
    async def levelup(self, ctx: commands.Context):
        level = level_up_poke(ctx.channel.name, ctx.author.name)
        poke = get_poke(ctx.channel.name, ctx.author.name)

        if not poke:
            await ctx.send(f'It seems {ctx.author.name} does not yet have a pokemon. Try ?pokegen')
            return
        if not level:
            await ctx.send(f'{ctx.author.name} has already leveled up {poke} this stream')
            return

        await ctx.send(f'{ctx.author.name}: your {poke} is now level {level}!') 
        

    @commands.command()
    async def pokeflex(self, ctx: commands.Context):
        pokemon = get_poke(ctx.channel.name, ctx.author.name)
        trainer = get_trainer(ctx.channel.name, ctx.author.name)
        if not pokemon:
            await ctx.send(f'It seems {ctx.author.name} does not yet have a pokemon. Try ?pokegen')

        await ctx.send(f'{ctx.author.name} is rocking a level {trainer["level"]} {pokemon}. Nice!')


    @commands.command()
    async def pep(self, ctx: commands.Context):
        if not ctx.channel.name == "dynamungo":
            await ctx.send(f"pep yourself {ctx.author.name} *copyright Phizzbot")

    @commands.command()
    async def pepify(self, ctx: commands.Context):
        if not ctx.channel.name == "dynamungo":
            phrase = ctx.message.content
            if phrase == '':
                return
            liz = phrase.split()
            i = 0
            for word in liz:
                if len(word) <= 3:
                    liz[i] = 'pep'
                i += 1
            new = ' '.join(liz)
            await ctx.send(new)










CobBot = Bot()

CobBot.run()

