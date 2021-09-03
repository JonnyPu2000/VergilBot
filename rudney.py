import discord
from discord import File
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

    while time != "19:26":
            print(time)
            time = datetime.datetime.now().strftime("%H:%M")
            sleep(2)

    if day.weekday() == 4 and time == "19:26":
        await channel.send(file = File("/assets/criaSexta.mp4"))
        await channel.send(file = File("/assets/shrekSexta.mp4"))

client.run(os.environ['DISCORD_TOKEN'])