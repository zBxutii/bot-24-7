import discord
import keep_alive
from discord.ext import commands

client = discord.Bot(command_prefix='.')

@client.event
async def on_ready():
  print('Bot Encendido.')
  
keep_alive.keep_alive()
client.run('token de tu bot')
