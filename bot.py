#!/usr/bin/python3

import discord, asyncio, os, platform, sys
from discord.ext import commands
from discord.ext.commands import Bot

if os.path.isfile("config.py"):
    import config
    
else:
    sys.exit("Config not found! Please add and try again.")


intents = discord.Intents().all()



bot = Bot(command_prefix=config.BOT_PREFIX, intents=intents)

@bot.event
async def on_ready():
    bot.loop.create_task(status_task())
    print(f"Logged in as {bot.user.name}")
    


async def status_task():
	while True:
		await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("You are Noob!"))
		await asyncio.sleep(50)
		await bot.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("You are supper Noob!!"))
		await asyncio.sleep(50)
		await bot.change_presence(status=discord.Status.online, activity=discord.Game(f"{config.BOT_PREFIX}help"))
		await asyncio.sleep(50)
		await bot.change_presence(status=discord.Status.do_not_disturb ,activity=discord.Game("I am Noob xD"))
		await asyncio.sleep(50)

# Remove default help command.
bot.remove_command("help")

if __name__ == "__main__":
    for extension in config.COGS:
        try:
            bot.load_extension(extension)
            extension = extension.replace("cogs.", "")
            print(f"Loaded extension '{extension}'")
        except Exception as e:
            exception = f"{type(e).__name__}: {e}"
            extension = extension.replace("cogs.", "")
            print(f"Failed to load extension {extension}\n{exception}")

@bot.command()
async def ping(context):
    '''
    This text will be shown in the help command
    '''

    await context.send(f'Pong! {round (bot.latency * 1000)} ms')


@bot.event
async def on_member_join(member):
    # print("Member" + member.name + "joined the server")
    
    welcomechannel = bot.get_channel(696601792288653374)
    
    embed=discord.Embed(
        title="A Deadly Hacker Arrived!",
        description= f"Congratulations on becoming the newest member of this server! Enjoy your stay & happy hacking! {member.mention}" + f"\n\nMake sure you check out #{bot.get_channel(815279320116363335)} and assign yourself some roles at #{bot.get_channel(815279326458937384)}" ,
        color=0xf18509
    )
    embed.set_footer(text="From N00B_4rMY with ❤️!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/815104420890279953/815150570372857876/Dark_bg.png")
    embed.set_author(name="👋 Welcome to N00B_4rMY!", url="https://noobarmy.org/")    
    await welcomechannel.send(embed=embed)

@bot.event
async def on_member_remove(member):

    log_channel = bot.get_channel(697659304026832973)
    embed=discord.Embed(
        title="A Deadly Hacker Left!",
        description= f"Goodbye {member.name}!",
        color=0xf18509
    )
    embed.set_footer(text="From N00B_4rMY with ❤️!")
    embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/815104420890279953/815150570372857876/Dark_bg.png")
    embed.set_author(name="👋 See you again!", url="https://noobarmy.org/")    
    await log_channel.send(embed=embed)





# Run the bot with the token
bot.run(config.TOKEN)