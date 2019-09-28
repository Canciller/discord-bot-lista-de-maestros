#!/bin/python

import sys

import discord
from dotenv import load_dotenv

from discord.ext import commands

import scraper

load_dotenv()
token = "DISCORD-TOKEN"

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'yegua')
async def command_yegua(ctx, *args):
    found = scraper.find('-'.join(args))
    if found:
        await ctx.send(found)

@bot.event
async def on_command_error(ctx, error):
    print(error)

def main():
    try:
        bot.run(token)
    except discord.errors.LoginFailure as e:
        print('Login failure:', e)
        sys.exit(1)
    except Exception as e:
        print('Error:', e)
        sys.exit(1)

if __name__ == "__main__":
    main()
