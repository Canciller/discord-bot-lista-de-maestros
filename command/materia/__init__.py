import discord
from discord.ext import commands

from . import scraper

async def function(ctx, *args):
    materia = scraper.find(' '.join(args))
    if materia:
        embed = discord.Embed(
                title = materia['name'],
                url = materia['url'],
                color = 0x21ea1f)

        await ctx.send(embed=embed)

command = commands.Command(function, name='materia')
