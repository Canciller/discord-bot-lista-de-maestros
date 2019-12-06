from discord.ext import commands

async def function(ctx, *args):
    await ctx.send("This is a test")

command = commands.Command(function, name='test')
