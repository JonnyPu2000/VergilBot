import discord
from discord import message
from discord.ext import commands
import datetime
import os
from time import sleep

client = commands.Bot(command_prefix = '.')
day = datetime.datetime.today()


@client.event
async def on_ready():
    print("Inicializado")
    

@client.event
async def on_message(message):
    if message.content.startswith('!hello'):
        embedVar = discord.Embed(title="Title", description="Desc", color=0x00ff00)
        embedVar.add_field(name="Field1", value="hi", inline=False)
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)



    #channel = client.get_channel(645698417544265769)
    #time = datetime.datetime.now().strftime("%H:%M")
    #while time != "18:09":
     #       print(time)
      #      time = datetime.datetime.now().strftime("%H:%M")
       #     sleep(1.5)

    #if day.weekday() == 4 and time >= "18:09":
     #       await channel.send(file)
      #      await channel.send("https://www.youtube.com/watch?v=8GX9--xhf_A")'''
    

    



#client.run(os.environ['DISCORD_TOKEN'])
client.run('ODgzMzI3OTUwMDgxMDk3NzI5.YTIVQg.chXPKvfzqCtgR_aBHixu9FJl3Wg')