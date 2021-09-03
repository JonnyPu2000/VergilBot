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
    time = datetime.datetime.now().strftime("%H:%M:%S")

    while True:
            time = datetime.datetime.now().strftime("%H:%M:%S")
            print(time)
            sleep(1)

            if day.weekday() == 4 and time == "20:58:00":
                        embed = Embed(title = "É Sexta Feira Meus Bacanos!",description = "SEXTA DOS CRIA PORRA",colour = colour.Colour.red())
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/criaSexta.mp4"))
                        await channel.send(file = File("./Assets/shrekSexta.mp4"))
        


client.run(os.environ['DISCORD_TOKEN'])