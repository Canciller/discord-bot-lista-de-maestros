#!/bin/python

import os
import sys

import discord
from dotenv import load_dotenv

from discord.ext import commands

import scraper

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name = 'yegua')
async def command_yegua(ctx, *args):
    maestros = scraper.find('-'.join(args))
    if maestros:
        message = []
        for maestro in maestros:
            await ctx.send(embed = maestro_embed(maestro))

@bot.event
async def on_command_error(ctx, error):
    print(error)

def maestro_embed(maestro):
    embed = discord.Embed(
            title = maestro['name'],
            url = maestro['url'],
            color = 0x21ea1f)

    embed.add_field(name='Chidos :thumbsup:', value=maestro['Chidos'], inline=True)
    embed.add_field(name='Gachos :thumbsdown:', value=maestro['Gachos'], inline=True)

    embed.add_field(name='Explicacion :pencil:', value=maestro['Explicacion'], inline=False)
    embed.add_field(name='Accesible :call_me:', value=maestro['Accesible'], inline=False)
    embed.add_field(name='Pasable :white_check_mark:', value=maestro['Pasable'], inline=False)
    embed.add_field(name='Asistencia :clock1:', value=maestro['Asistencia'], inline=False)
    embed.add_field(name='Sexy :fire:', value=maestro['Sexy'], inline=False)

    return embed;

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
