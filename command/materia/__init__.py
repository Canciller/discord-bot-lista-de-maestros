import discord
from discord.ext import commands

from . import scraper

async def function(ctx, *args):
    materia = scraper.find(' '.join(args))
    if materia:
        await ctx.send(materia)

command = commands.Command(function, name='materia')
