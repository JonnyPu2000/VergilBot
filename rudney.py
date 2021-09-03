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


    channel = client.get_channel(645698417544265769)
    time = datetime.datetime.now().strftime("%H:%M")

    while time != "19:07":
            print(time)
            time = datetime.datetime.now().strftime("%H:%M")
            sleep(2)

    if day.weekday() == 4 and time == "19:07":
        embedVar = discord.Embed(title="Sexta dos CRIA", description="É sexta feira meus bacanos!!! \nhttps://www.youtube.com/watch?v=pCTSdupScwA", color=0x00ff00)
        await channel.send(embed=embedVar)

client.run(os.environ['DISCORD_TOKEN'])