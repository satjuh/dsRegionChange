import os
import discord

from discord.ext import commands
from dotenv import load_dotenv

# Load token form .env file
load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')
client = discord.Client()
regs = [i.name.replace("_", "-")
        for i in discord.VoiceRegion if "vip" not in i.name]


# Change region if it's in discord regions enum
@bot.command(name='region')
async def changeRegion(ctx, reg):
    guild = ctx.guild
    if reg.lower() in regs:
        await guild.edit(region=reg)
        await ctx.send('Changing region to ' + reg)
    else:
        await ctx.send('No such region')


# Print all available regions
@bot.command(name='regions')
async def regions(ctx):
    await ctx.send(', '.join(regs))

bot.run(token)
