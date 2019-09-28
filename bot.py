import os
import sys

import discord
from dotenv import load_dotenv

load_dotenv()
token = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(client.guilds)
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

try:
    client.run(token)
except discord.errors.LoginFailure as e:
    print('Login failure:', e)
    sys.exit(1)
except KeyboardInterrupt:
    sys.exit()
except Exception as e:
    print('Error:', e)
    sys.exit(1)
