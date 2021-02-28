import os, sys, discord, time, asyncio
from discord.ext import commands
if not os.path.isfile("config.py"):
    sys.exit("Config not found! Please add and try again.")
else:
    import config



class moderation(commands.Cog, name="moderation"):
    def __init__(self, bot):
        self.bot = bot

    
    

    @commands.command(name='kick', pass_context=True)
    async def kick(self, context, member: discord.Member, *args):
        serverupdate_channel = self.bot.get_channel(760243939688185907)
        if context.message.author.guild_permissions.kick_members:
            if member.guild_permissions.administrator:
                embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description = f"Hahaha! So funny! You don't have access to do that LMAO!! 🤣",
                    color=0xf10909
                )
                await context.send(embed=embed, delete_after=5)
                #await context.message.delete()
                
            else:
                try:
                    reason = " ".join(args)
                    
                    embed = discord.Embed(
                        title = "✅ User Kicked!",
                        description = f"A wild shit named **{member}** was kicked by **{context.message.author}**!",
                        color=0x09f118
                    )
                    embed.add_field(
                        name = "Reason: ",
                        value = reason
                    )

                    await serverupdate_channel.send(embed=embed)
                    await context.message.delete()
                    try:
                        
                        await member.send(
                            f"You have been kicked out from N00B_4rMY by **{context.message.author}** due to,\nReason: {reason}"
                        )
                        await member.kick()
                    except:
                        pass
                except:
                    embed = discord.Embed(
                        title = "⛔️ Error!!",
                        description = f"An Error occurred while trying to kick the user.\n Check if you have used the right command - `$kick @user <reason>`",
                        color=0xf10909
                    )
                    await context.message.channel.send(embed=embed, delete_after=5)
                    await context.message.delete()
        else:
            embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description= f"Hahaha! So funny! You don't have access to do that LMAO!! 🤣",
                    color=0xf10909
                )
            await context.send(embed=embed, delete_after=5)
            await context.message.delete()
    


    @commands.command(name="ban", pass_context=True)
    async def asd(self, context, member: discord.Member, *args):
        serverupdate_channel = self.bot.get_channel(760243939688185907)
        if context.message.author.guild_permissions.administrator:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description= f"Hahaha! So funny! You don't have access to do that LMAO!! 🤣",
                    color=0xf10909
                )
                    await context.send(embed=embed, delete_after=5)
                    await context.message.delete()
                else:
                    
                    reason = " ".join(args)
                    
                    embed = discord.Embed(
                        title="🚫 User Banned!",
                        description=f"A wild shit named **{member}** was Banned by **{context.message.author}**!",
                        color=0xf00c23
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    await serverupdate_channel.send(embed=embed)
                    await context.message.delete()
                    await member.send(f"You have been Banned from N00B_4rMY by **{context.message.author}** due to \nReason: {reason}")
                    await member.ban(reason=reason)
                    await member.ban()
                    
                    
            except:
                embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description = f"An Error occurred while trying to Ban the user.\n Check if you have used the right command - `$ban @user <reason>`",
                    color=0xf10909
                )
                await context.send(embed=embed, delete_after=5)
                await context.message.delete()
        else:
            embed = discord.Embed(
                title = "⛔️ Error!! ⛔️",
                description= f"Hahaha! So funny! You don't havsee access to do that LMAO!! 🤣",
                color=0xf10909
            )
            await context.send(embed=embed, delete_after=5)
            await context.message.delete()

    

    @commands.command(name="warn")
    async def ban(self, context, member: discord.Member, *args):
        serverupdate_channel = self.bot.get_channel(760243939688185907)
        if context.message.author.guild_permissions.administrator:
            try:
                if member.guild_permissions.administrator:
                    embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description= f"Hahaha! So funny! You don't have access to do that LMAO!! 🤣",
                    color=0x09f118
                )
                    await context.send(embed=embed, delete_after=5)
                    await context.message.delete()
                else:
                    
                    reason = "".join(args)
                    
                    embed = discord.Embed(
                        title="⚠️ User Warned! ⚠️",
                        description=f"**{member.mention}** was warned by **{context.message.author}**!",
                        color=0xe2f109
                    )
                    embed.add_field(
                        name="Reason:",
                        value=reason
                    )
                    
                    await serverupdate_channel.send(embed=embed)
                    await context.message.delete()
                    await member.send(f"You have been Warned at N00B_4rMY by **{context.message.author}** due to \nReason: {reason}")
                    
            except:
                embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description = f"An Error occurred while trying to Warn the user.\n Check if you have used the right command - `$warn @user <reason>`",
                    color=0xf10909
                )
                await context.send(embed=embed, delete_after=5)
                await context.message.delete()
        else:
            embed = discord.Embed(
                title = "⛔️ Error!! ⛔️",
                description= f"Hahaha! So funny! You don't have access to do that LMAO!! 🤣",
                color=0xf10909
            )
            await context.send(embed=embed, delete_after=5)
            await context.message.delete()


    
    @commands.command(name="purge")
    async def abc(self, context, number):
        if context.message.author.guild_permissions.administrator:
            try:
                number = int(number)
            except:
                embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description = f"`{number}` is not a valid number.",
                    color=0xf10909
                )
                await context.send(embed=embed, delete_after=5)
                await context.message.delete()

                return
            if number < 1:
                embed = discord.Embed(
                    title = "⛔️ Error!!",
                    description = f"`{number}` message can't be deleted.",
                    color=0xf10909
                )
                await context.send(embed=embed, delete_after=5)                
                await context.message.delete()

                return
            purged_messages = await context.message.channel.purge(limit=number)
            embed = discord.Embed(
                title = "🗑️ Chat Cleared!",
                description = f"**{context.message.author}** cleared **{len(purged_messages)}** messages!",
                color=0x09f118
            )
            await context.send(embed=embed, delete_after=5)
            await context.message.delete()
            
        else:
            embed = discord.Embed(
                title = "⛔️ Error!!",
                description = "You don't have the permission to use this command.",
                color = 0xf10909
            )
            msg = await context.send(embed=embed, delete_after=5)
            await context.message.delete()

def setup(bot):
    bot.add_cog(moderation(bot))