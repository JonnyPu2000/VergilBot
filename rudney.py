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

@client.event
async def on_ready():
    print("Inicializado")


    channel = client.get_channel(645698417544265769)
    time = datetime.datetime.now().strftime("%H:%M:%S")

    while True:
        
            time = datetime.datetime.now().strftime("%H:%M:%S")
            day = datetime.datetime.today()
            print(time)
            sleep(1)

            if day.weekday() == 0 and time == "16:21:00":
                await channel.send(file = File("./Assets/capivarinhas.mp4"))

            if day.weekday() == 4 and time == "15:00:00":
    
                        embed = Embed(title = "É SEXTA FEIRA MEUS BACANOS!",description = "SEXTA DOS CRIA PORRA",colour = colour.Colour.red())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://c.tenor.com/J5O9kElWluYAAAAC/mucalol-smurfdomuca-muca-muquinha-dan%C3%A7ando-dan%C3%A7a-dancing-macaco-macacolol.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/criaSexta.mp4"))
                        await channel.send(file = File("./Assets/shrekSexta.mp4"))
        


client.run(os.environ['DISCORD_TOKEN'])
#client.run('ODgzMzI3OTUwMDgxMDk3NzI5.YTIVQg.chXPKvfzqCtgR_aBHixu9FJl3Wg')
