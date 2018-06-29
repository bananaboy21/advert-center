import discord
import os
from discord.ext import commands


bot = commands.Bot(command_prefix="+",owner_id=277981712989028353)


@bot.event
async def on_ready():
    print('Bot is online, and ready to ROLL!')
    
    
@bot.command
async def dmall(self, ctx, msg: str):
    msg = await ctx.send("Please wait, DMing everyone...")
    for x in ctx.guild.members:
        await x.send(msg)
    await msg.edit(content="Successfully DMed everyone.")
    
    
bot.run(os.environ.get("TOKEN"))
