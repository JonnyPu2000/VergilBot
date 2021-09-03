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

    while time != "19:13":
            print(time)
            time = datetime.datetime.now().strftime("%H:%M")
            sleep(2)

    if day.weekday() == 4 and time == "19:13":
        embedVar = discord.Embed.video(url = "https://www.youtube.com/watch?v=pCTSdupScwA")
        await channel.send(embed=embedVar)

client.run(os.environ['DISCORD_TOKEN'])