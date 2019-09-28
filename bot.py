import os
import time
import sys

import requests

import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'yegua')
async def command_yegua(ctx, *args):
    await ctx.send(' '.join(args))

@bot.event
async def on_command_error(ctx, error):
    print(error)

try:
    bot.run(token)
except discord.errors.LoginFailure as e:
    print('Login failure:', e)
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    print('Error:', e)
    sys.exit(1)
