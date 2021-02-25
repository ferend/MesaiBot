import discord
import os
import asyncio
import logging
import re



logger = logging.getLogger()
client = discord.Client()
client.TIMERS = {}



@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith("Fselam"):
    
    await message.channel.send("As.")
  
  if msg.startswith("Fmaas"):
    
    await message.channel.send("www.nesine.com")

  if msg.startswith("Fplay"):
    
    await message.channel.send("https://www.youtube.com/watch?v=YbRc_0V-6nQ&ab_channel=Atrax")      
    


client.run(os.getenv('TOKEN'))



