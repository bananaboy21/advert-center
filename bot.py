import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="+",owner_id=277981712989028353)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    
    
@bot.command()
async def dmall(ctx, *, msg: str):
    if not "CEO" in [x.name for x in ctx.author.roles]:
        return await ctx.send("NOPE! You must have the CEO role to use this command.")
    msg = await ctx.send("Please wait, DMing everyone...")
    for x in ctx.guild.members:
        try: await x.send(msg)
        except: continue
    await msg.edit(content="Successfully DMed everyone.")
    
    
bot.run(os.environ.get("TOKEN"))
