import os, sys, discord
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("Config not found! Please add and try again.")
else:
    import config

class Help(commands.Cog, name="help"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="help")
    async def help(self, context):


        prefix = config.BOT_PREFIX
        if not isinstance(prefix, str):
            prefix = prefix[0]
        
        embed = discord.Embed(

            title = "General Commands: ",
            description = f"`$help`- Display all available commands that can be run.\n" + f"`$rules`- List all Server Rules.\n" + f"`$serverinfo`- DM's what this server is all about.\n" + f"`$gen_code` - Sends you an invite code in your DM.\n",
            color = 0xf18509
    )

        embed.add_field(
            name = "Moderation Commands: ",
            value = f"`$kick @user <Reason>`- Kick an user, Must have required Permission to Kick Members.\n" + f"`$ban @user <Reason>`- Ban an user, Must have required Permission to Ban Members.\n" + f"`$warn @user <Reason>`- Warn an user, Must have required Permission to Warn Members.\n" + f"`$purge <number>`- Purge a specified number of message. Must have required Permission to Delete Message\n" + f"`$poll <Details>` - Creates a Poll! You must have Administrator Permission to use this.",
            inline=False
        )

        embed.add_field(
            name = "Fun Commands: ",
            value = f"`$8ball`- Ask a random question to get a random answer.\n" + f"`$ping` - Responds with bot's latency\n",
            inline=False
        )
        embed.set_footer(text="From N00B_4rMY with ❤️!")
        #embed.set_image(url="https://cdn.discordapp.com/attachments/815104420890279953/815150570372857876/Dark_bg.png")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/815104420890279953/815150570372857876/Dark_bg.png")
        embed.set_author(name='⚙️ N00B_4rMY - Bot Commands')

        await context.send(embed=embed)

def setup(bot):
    bot.add_cog(Help(bot))