import os, sys, discord, platform, random, aiohttp, json
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("'config.py' not found! Please add it and try again.")
else:
    import config

class rules(commands.Cog, name="rules"):
    def __init__(self, bot):
        self.bot = bot


    @commands.command(name="rules")
    async def rules(self, context):
        embed = discord.Embed(
            title = "How it Works??",
            description = f"If you break a rule(s) you will get a warning message by an admin, if you continue this will lead depending on the rule to mute/kick or to a permanently ban.",
            color = 0xf18509
        )
        embed.add_field(name="1.", value=f"No direct messages (DMs) to other members of the discord. This includes admins. Verify that the member you are messaging is ok with you sending them DMs. Keep conversations Safe for work. This is an educational and professional environment, make sure that your words do not make other members uncomfortable.\n", inline=False)
        embed.add_field(name="2.", value=f"Racism is not tolerated and will result in a permanent ban.\n", inline=False)
        embed.add_field(name="3.", value=f"No self Promotion, No advertisement. First contact admins , if allowed then admins will post according to them.\n", inline=False)
        embed.add_field(name="4.", value=f"Administrators reserve the right to modify the rules at any time and extend them accordingly to conditions which may not be currently included in these rules.\n", inline=False)
        embed.add_field(name="5.", value=f"Do not post viruses or malicious files without explicit permission from the admins.\n", inline=False)
        embed.add_field(name="6.", value=f"Do not ask for any black-hat related services. This includes sharing links to pirated data, sharing cracks, committing copyright violation, or breaking into accounts and any form of cyber attack.. We neither support nor indulge ourselves into these activities. We will report these incidents to the concerned authorities.\n", inline=False)
        embed.add_field(name="7.", value=f"Using emote is not prohibited but that should not be improper.\n", inline=False)
        embed.add_field(name="8.", value=f"When asking for help or support please perform research to your fullest ability. Community Mentors have the right to refuse helping those who have not done research on their own first.\n", inline=False)
        embed.add_field(name="9.", value=f"Be clear to the questions. Ask point to point questions.", inline=False)



        embed.set_author(name='📜 N00B_4rMY Server Rules!📜')
        embed.set_footer(text="From N00B_4rMY with ❤️!")
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/815104420890279953/815150570372857876/Dark_bg.png")

        await context.send("Check your DM! {}".format(context.message.author.mention, delete_after=5))
        await context.author.send(embed=embed)
        await context.message.delete()



def setup(bot):
    bot.add_cog(rules(bot))