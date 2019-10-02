#!/bin/python

import os
import sys

import discord
from dotenv import load_dotenv

from discord.ext import commands

import scraper

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

error_log = os.getenv('ERROR_LOG_PATH')
guild_log = os.getenv('GUILD_LOG_PATH')

bot = commands.Bot(command_prefix = '!')

def log(path : str, message : str):
    try:
        with open(path, 'a') as file:
            file.write(f'{message}\n')
    except EnvironmentError as e:
        print(e)

    print(message)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.event
async def on_guild_join(guild):
    log(guild_log, f'[join] {guild}')

@bot.event
async def on_guild_remove(guild):
    log(guild_log, f'[remove] {guild}')

@bot.event
async def on_guild_available(guild):
    log(guild_log, f'[available] {guild}')


@bot.command(name = 'maestro')
async def command_yegua(ctx, *args):

    maestros = scraper.find('-'.join(args))
    if maestros:
        for maestro in maestros:
            await ctx.send(embed = maestro_embed(maestro))

@bot.event
async def on_command_error(ctx, error):
    log(error_log, error)
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
