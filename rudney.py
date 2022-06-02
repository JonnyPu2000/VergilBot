import discord
from discord import File, Embed
from discord import message
from discord import colour
from discord import channel
from discord.embeds import Embed
from discord.ext import commands, tasks
import datetime
import os
from time import sleep
import random
from discord import FFmpegPCMAudio
from asyncio import sleep

#Teste2ss
client = commands.Bot(command_prefix = '%')

@client.event
async def on_ready():
    
    print("Inicializado")

@client.command()
async def balls(ctx):
    await ctx.send(file = File('./Assets/balls.mp4'))

@client.command()
async def sigma(ctx):
    await ctx.send(file = File('./Assets/sigma.mp4'))

@client.command()
async def foto(ctx):
    await ctx.send(file = File('./Assets/foto.mp4'))


@client.command()
async def tv(ctx):
    await ctx.send(file = File('./Assets/television.mp4'))


@client.command()
async def start(ctx,enabled = "start",interval = 1,message = ""):
    if enabled.lower() == "stop":
        mandaDia.stop()
    elif enabled.lower() == "start":
        mandaDia.change_interval(seconds= int(interval))
        mandaDia.start()


@tasks.loop(seconds = 1)
async def mandaDia():

    await client.wait_until_ready()

    channel = client.get_channel(645698417544265769)

    hora = datetime.datetime.now().strftime("%H:%M:%S")
    day = datetime.datetime.today()
    print(hora)

    if hora == "03:00:00":
        await channel.send(file = File("./Assets/macacoOleo.mp4"))

    #Segunda Feira
    if day.weekday() == 0 and hora == "11:00:00":
                embed = Embed(title = "VAMO TRABALHAR BANDO DE VAGABUNDO",description = "CADE MINHAS CAPIVARINHAS???",colour = colour.Colour.blue())
                embed.set_image(url = "https://c.tenor.com/K3uxrqffdCAAAAAC/capybara-orange.gif")
                embed.set_footer(text= "Crias do Xamil", icon_url= "https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                await channel.send(embed = embed)
                await channel.send(file = File("./Assets/capivarinhas.mp4"))
            
    #Terça
    if day.weekday() == 1 and hora == "15:00:00":
    
                        embed = Embed(title = "É MAMACO-FEIRA MEUS BACANOS!",description = "UUUUUUUUUU AAAAAAA AAAAAAAAAAAA UUUUUU AAAAAAAA",colour = colour.Colour.dark_red())
                        embed.set_footer(text= "XAMIL MAMACOs",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_thumbnail(url="https://c.tenor.com/bB0vUlhGjygAAAAS/monkey-drinking.gif")
                        embed.set_image(url= "https://c.tenor.com/sRi4JysBEmUAAAAS/monkiflip-monki.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/monkeTerca.mp4"))
            
    #Quarta
    if day.weekday() == 2 and hora == "15:00:00":
    
                        embed = Embed(title = "É QUARTA FEIRA MEUS BACANOS!",description = "QUASE LÁ",colour = colour.Colour.dark_purple())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url = "https://media.discordapp.net/attachments/837207335453458432/843647622165692426/TURKEY.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/quartaXeira.mp4"))

    #Quinta
    if day.weekday() == 3 and hora == "15:00:00":
    
                        embed = Embed(title = "SIGMA FEIRA",description = "ASTROTRILLIONAIRE GRINDSET",colour = colour.Colour.dark_grey())
                        embed.set_thumbnail(url= "https://media1.giphy.com/media/t9lBEE2FGMzbY9s5IX/giphy.gif?cid=ecf05e47dq4kzvsg08scf1gj3pfxqm227dg07doiumgickeo&rid=giphy.gif&ct=g")
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url = "https://c.tenor.com/Q823-830Ri0AAAAd/christian-bale-american-psycho.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/sigmaMale.mp4"))
            

    #Sexta
    if day.weekday() == 4 and hora == "15:00:00":
    
                        embed = Embed(title = "É SEXTA FEIRA MEUS BACANOS!",description = "SEXTA DOS CRIA PORRA",colour = colour.Colour.red())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://c.tenor.com/J5O9kElWluYAAAAC/mucalol-smurfdomuca-muca-muquinha-dan%C3%A7ando-dan%C3%A7a-dancing-macaco-macacolol.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/criaSexta.mp4"))
                        await channel.send(file = File("./Assets/shrekSexta.mp4")) 

    #Sábado
    if day.weekday() == 5 and hora == "15:00:00":
        
                        embed = Embed(title = "SABADO FEMBOY",description = "SÓ AS GOSTOSAS",colour = colour.Colour.red())
                        embed.set_footer(text= "XAMIL FEMBOY",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://c.tenor.com/7kyzvgcZg6gAAAAd/f1nn5ter-rose.gif")
                        embed.set_thumbnail(url="https://c.tenor.com/N2W5LJ4SdMEAAAAC/muah-kisses.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/ZeroTwo.mp4"))

@client.command()
async def rock(ctx):
    rand = random.randint(0,1)

    if rand == 0:
        await ctx.send(file = File("./Assets/theRock.mp4"))

    if rand == 1:
        await ctx.send(file = File("./Assets/theRock2.mp4"))

@client.command()
async def comedia(ctx):
    await ctx.send(file = File("./Assets/MestreDaComedia.mp4")) 

@client.command()
async def omg(ctx):
    await ctx.send(file = File("./Assets/omg.mp4"))   

@client.command()
async def sam(ctx):
    await ctx.send(file = File("./Assets/there will be blood shed.mp4"))   

@client.command()
async def dmc(ctx):
    await ctx.send(file = File("./Assets/vergil.mp4"))

@client.command()
async def standinghere(ctx):
    await ctx.send(file = File("./Assets/bracoforte.mp4"))

@client.command()
async def fma(ctx):
    await ctx.send(file = File("./Assets/fma.mp4"))

@client.command()
async def saul(ctx):
    rand = random.randint(0,1)

    if rand == 0:
        await ctx.send(file = File("./Assets/saul 8bits.mp4"))

    if rand == 1:
        await ctx.send(file = File("./Assets/Saul goodman 3d.mp4"))      

@client.command(pass_context=True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        await ctx.send("Você não está em um canal de voz, burro!")


@client.command(pass_context=True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("Sai do canal")
    else:
        await ctx.send("Eu não tô em um canal de voz, burro!")

@client.command()
async def faro(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/faro.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def cavalo(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/cavalo.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def iha(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/iha.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def danca(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/danca.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def leite(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/muito-leite.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def pare(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/pare.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def ph(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/ph.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def pressao(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/pressaoNenem.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def puta(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/puta.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def goofy(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/rodrigo-faro-sound.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def sla(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/sla.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def titio(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/titio.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def tome(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/tome.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def uepa(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/uepa.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def ui(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/ui-rodrigo-faro.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def elegosta(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/elegosta.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")

@client.command()
async def queisso(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/que isso meu filho calma.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect()      
    else:
        await ctx.send("Não ta num canal de voz o seu animal!")



client.run('ODgzMzI3OTUwMDgxMDk3NzI5.YTIVQg.chXPKvfzqCtgR_aBHixu9FJl3Wg')