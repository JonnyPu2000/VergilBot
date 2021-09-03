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


    channel = client.get_channel(883328580455637045)
    time = datetime.datetime.now().strftime("%H:%M")

    while time != "19:56":
            print(time)
            time = datetime.datetime.now().strftime("%H:%M")
            sleep(2)

    if day.weekday() == 4 and time == "19:56":
        embed = Embed(title = "É Sexta Feira Meus Bacanos!",description = "SEXTA DOS CRIA PORRA",colour = colour.Colour.red())
        await channel.send(embed = embed)
        await channel.send("https://www.youtube.com/watch?v=pCTSdupScwA")
        await channel.send("https://www.youtube.com/watch?v=8GX9--xhf_A")
        


client.run(os.environ['DISCORD_TOKEN'])