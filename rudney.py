import discord
from discord import File, Embed
from discord import message
from discord import colour
from discord.embeds import Embed
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

    while time != "19:39":
            print(time)
            time = datetime.datetime.now().strftime("%H:%M")
            sleep(2)

    if day.weekday() == 4 and time == "19:39":
        embed = Embed(title = "É Sexta Feira Meus Bacanos!",description = "SEXTA DOS CRIA PORRA",colour = colour.Colour.red())
        embed.video(File("./Assets/criaSexta.mp4"))
        embed.video(File("./Assets/shrekSexta.mp4"))
        await channel.send(embed)


client.run(os.environ['DISCORD_TOKEN'])