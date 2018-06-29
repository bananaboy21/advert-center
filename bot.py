import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="+",owner_id=277981712989028353)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    
    
@bot.command()
async def dmall(ctx, *, msg):
    if not "CEO" in [x.name for x in ctx.author.roles]:
        return await ctx.send("NOPE! You must have the CEO role to use this command.")
    m = await ctx.send("Please wait, DMing everyone...")
    for x in ctx.guild.members:
        try: await x.send(str(msg))
        except: continue
    await m.edit(content=f"**Message sent.**\n\nServer name : {ctx.guild.name}\nWriter : {ctx.author.name}\nTime : {str(message.created_at).split('.')[0]}\nMessage : {str(msg)}")
    
bot.run(os.environ.get("TOKEN"))
