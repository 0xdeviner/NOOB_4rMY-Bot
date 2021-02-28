import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config


class game(commands.Cog, name="game"):
    def __init__(self, bot):
        self.bot = bot
    
        
        
    def check_tag(context):
        return not any(m in context.message.content for m in ["@here", "@everyone"])

    @commands.command(aliases=['8ball', '8Ball'])
    @commands.check(check_tag)
    async def _8ball(self, context, *, message: commands.clean_content):

        answers = ['It is certain.', 'It is decidedly so.', 'You may rely on it.', 'Without a doubt.',
                   'Yes - definitely.', 'As I see, yes.', 'Most likely.', 'Outlook good.', 'Yes.',
                   'Signs point to yes.', 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.',
                   'Cannot predict now.', 'Concentrate and ask again later.', 'Don\'t count on it.', 'My reply is no.',
                   'My sources say no.', 'Outlook not so good.', 'Very doubtful.']
        
        response = random.choice(answers)
        embed = discord.Embed(
            title = "🎮 I am Oracle",
            description=f"**Your Question:** {message}\n\n" + f"**My Answer:** {response}",
            color = 0x4000ff
        )
        await context.send(embed=embed)


    @commands.command(name="meme")
    async def meme(self, context):
        embed = discord.Embed(title="Enjoy a Meme", description="Meme", color=0xf18509)
        async with aiohttp.ClientSession() as me:
            async with me.get('https://www.reddit.com/r/dankmemes/new.json?sort=hot') as r:
                result = await r.json()
                embed.set_image(url=result['data']['children'] [random.randint(0, 30)]['data']['url'])
                await context.send(embed=embed)
                await context.message.delete()

def setup(bot):
    bot.add_cog(game(bot))