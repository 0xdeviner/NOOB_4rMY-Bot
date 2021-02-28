import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class general(commands.Cog, name="general"):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="serverinfo")
    async def serverinfo(self, context):
        embed = discord.Embed(
            name = "N00B_4rMY",
            description = "**N00B_4rMY is an Information Security Open Source Community. We help each other to learn security stuff and be the best version of ourselves as well as others. This community was created to help those newbies out there who are struggling to take a step ahead in CyberSec fields and learn stuffs which leads them to become a PRO from just a NOOB. \nWe try our best to help them get started in this vast matrix of CYBER SECURITY in a non-profitable way. If you are interested in Pentesting, Bug Hunting, CTFs, Programming, or any sort of collaboration with like-minded people out there, then you are at the right place. We are an open source community and We would love to welcome all hats as this is a place Learn and Educate.**",
            color = 0xf18509
        )
        
        embed.add_field(name='Twitter', value='**[Follow us on Twitter](https://www.twitter.com/noobarmy_)**',inline=False)
        embed.add_field(name='Instagram', value='**[Follow us on Instagram](https://www.instagram.com/noobarmy__)**',inline=False)
        embed.add_field(name='Website', value='**[Our Website](https://noobarmy.org/)**',inline=False)
        embed.add_field(name='Discord', value='**[Join Discord](https://discord.gg/fNyS38fwJr)**',inline=False)

        embed.set_footer(text="From N00B_4rMY with ❤️!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/815104420890279953/815150570372857876/Dark_bg.png")
        embed.set_author(name=" N00B_4rMY", url="https://noobarmy.org/")


        await context.send("Check your DM! {}".format(context.message.author.mention, delete_after=5))
        await context.author.send(embed=embed)
        await context.message.delete()
        

    @commands.command(name="gen_code")
    async def server(self, context):
        """
        Get the invite link of the discord server of the bot for some support.
        """
        await context.send("Check your DM! {}".format(context.message.author.mention, delete_after=5) )
        await context.author.send("Join N00B_4rMY's discord server by clicking here: https://discord.gg/fNyS38fwJr")
        await context.message.delete()



    @commands.command(name="poll")
    async def poll(self, context, *args):
        if context.message.author.guild_permissions.administrator:
            try:       
                poll_title = " ".join(args)
                embed = discord.Embed(
                    title=f"A new poll has been created!",
                    description=f"**{poll_title}**",
                    color=0xf18509
                )
                embed.set_footer(
                    text=f"Poll created by: {context.message.author} • React to vote!"
                )
                embed_message = await context.send(embed=embed)
                await embed_message.add_reaction("👍")
                await embed_message.add_reaction("👎")
                await embed_message.add_reaction("🤷")
            except:
                pass
        else:
            embed = discord.Embed(
                title = "⛔️ Error!!",
                description = "You don't have the permission to use this command.",
                color = 0xf10909
            )
            msg = await context.send(embed=embed, delete_after=5)
            await context.message.delete()



def setup(bot):
    bot.add_cog(general(bot))