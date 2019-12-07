import discord
from discord.ext import commands

from . import scraper

def embed(maestro):
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

async def function(ctx, *args):
    maestros = scraper.find('-'.join(args))
    if maestros:
        for maestro in maestros:
            await ctx.send(embed = embed(maestro))

command = commands.Command(function, name='maestro')
