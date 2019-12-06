import os
from dotenv import load_dotenv

load_dotenv()
def getenv(variable):
    return os.getenv(variable)

token = getenv('DISCORD_TOKEN')
command_prefix = '!'

logging_format = '%(asctime)s:%(levelname)s:%(name)s: %(message)s'
