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
    testChannel = client.get_channel(883328580455637045)


    time = datetime.datetime.now().strftime("%H:%M:%S")

    while True:
        
            time = datetime.datetime.now().strftime("%H:%M:%S")
            day = datetime.datetime.today()
            print(time)
            sleep(1)

            if time == "03:00:00":
                await channel.send(file = File("./Assets/macacoOleo.mp4"))

            #Segunda Feira
            if day.weekday() == 0 and time == "11:00:00":
                embed = Embed(title = "VAMO TRABALHAR BANDO DE VAGABUNDO",description = "CADE MINHAS CAPIVARINHAS???",colour = colour.Colour.blue())
                embed.set_image(url = "https://c.tenor.com/K3uxrqffdCAAAAAC/capybara-orange.gif")
                embed.set_footer(text= "Crias do Xamil", icon_url= "https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                await channel.send(embed = embed)
                await channel.send(file = File("./Assets/capivarinhas.mp4"))
            
            #Terça
            if day.weekday() == 1 and time == "15:00:00":
    
                        embed = Embed(title = "É TERÇA FEIRA MEUS BACANOS!",description = "TERÇA DOS CRIA PORRA",colour = colour.Colour.red())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://c.tenor.com/49dE7BLNWy4AAAAd/gabriel-monteiro-gabriel.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/criaTerca.mp4"))
            
            #Quarta
            if day.weekday() == 2 and time == "15:00:00":
    
                        embed = Embed(title = "É QUARTA FEIRA MEUS BACANOS!",description = "QUASE LÁ",colour = colour.Colour.dark_purple())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url = "https://media.discordapp.net/attachments/837207335453458432/843647622165692426/TURKEY.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/quartaXeira.mp4"))

            #Quinta
            if day.weekday() == 2 and time == "19:25:00":
    
                        embed = Embed(title = "SIGMA FEIRA",description = "ASTROTRILLIONAIRE GRINDSET",colour = colour.Colour.black())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url = "https://c.tenor.com/Q823-830Ri0AAAAd/christian-bale-american-psycho.gif")
                        await testChannel.send(embed = embed)
                        await testChannel.send(file = File("./Assets/sigmaMale.mp4"))
            

            #Sexta
            if day.weekday() == 4 and time == "15:00:00":
    
                        embed = Embed(title = "É SEXTA FEIRA MEUS BACANOS!",description = "SEXTA DOS CRIA PORRA",colour = colour.Colour.red())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://c.tenor.com/J5O9kElWluYAAAAC/mucalol-smurfdomuca-muca-muquinha-dan%C3%A7ando-dan%C3%A7a-dancing-macaco-macacolol.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/criaSexta.mp4"))
                        await channel.send(file = File("./Assets/shrekSexta.mp4"))
        


client.run(os.environ['DISCORD_TOKEN'])
#client.run('ODgzMzI3OTUwMDgxMDk3NzI5.YTIVQg.chXPKvfzqCtgR_aBHixu9FJl3Wg')
