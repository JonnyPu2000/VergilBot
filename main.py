#Importando Bibliotecas

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
from pytube import YouTube
from moviepy.editor import VideoFileClip, concatenate_videoclips
import shutil

        


#Prefixo para comandoss
client = commands.Bot(command_prefix = '%')


#Inicializando o Bot
@client.event
async def on_ready():
    
    print("Inicializado")


#Inicializando o Relógio (contador)
@client.command()
async def start(ctx,enabled = "start",interval = 1,message = ""):
    if enabled.lower() == "stop":
        mandaDia.stop()
    elif enabled.lower() == "start":
        mandaDia.change_interval(seconds= int(interval))
        mandaDia.start()
    


@client.command()
async def play(ctx,link,chn = None):

    def remove_special_characters(title):
        new_title =  ''.join(char for char in title if char.isalnum()) #Removendo todos os caracteres especiais, deixando apenas as letras
        return new_title


    def download_yt(link):
        video = YouTube(link)
        title = remove_special_characters(video.title)
        stream = video.streams.get_highest_resolution()
        stream.download("audio/",filename= title + ".mp4")
        ctx.send("Download realizado com sucesso!")
        return title
    
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    title = download_yt(link)
    
    videoclip = VideoFileClip("audio/" + title + '.mp4')
    audioclip = videoclip.audio
    audioclip.write_audiofile("audio/" + title + '.mp3')


    source = FFmpegPCMAudio("audio/" + title + ".mp3")

    voice = await channel.connect()
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect()
    os.system("pkill -f ffmpeg")
    shutil.rmtree("./audio")

#Função de juntar dois videos, passando o link do video do youtube
@client.command()
async def vergil(ctx, link,x,y):
    await ctx.send("Vergilizando o seu vídeo, por favor aguarde!")
    #Removendo os caracteres especiais do link
    def remove_special_characters(title):
        new_title =  ''.join(char for char in title if char.isalnum()) #Removendo todos os caracteres especiais, deixando apenas as letras
        return new_title



    #Função de Download do video, utilizando a biblioteca pytube
    def download_yt(link):
        video = YouTube(link)
        title = remove_special_characters(video.title)
        stream = video.streams.get_highest_resolution()
        stream.download("videos/",filename= title + ".mp4")
        ctx.send("Download realizado com sucesso!")
        return title

    

    def edit_video(link):
        title = download_yt(link)
        video = VideoFileClip("videos/" + title + ".mp4")
        clip = VideoFileClip("videos/" + title + ".mp4").subclip(x,y)
        
        clip2 = VideoFileClip("Assets/vergil_src.mp4").subclip(0,45)
        clips = [clip, clip2]
        ctx.send("Criando o clipe, por favor aguarde...")
        combined = concatenate_videoclips(clips, method= 'compose')
        combined.write_videofile("videos/combined.mp4")
        os.system("pkill -f ffmpeg")

    edit_video(link)
    await ctx.send(file = File("videos/combined.mp4"))
    shutil.rmtree("./videos")
    
        


@tasks.loop(seconds = 1)
async def mandaDia():

    await client.wait_until_ready()

    channel = client.get_channel(645698417544265769)

    hora = datetime.datetime.now().strftime("%H:%M:%S")
    day = datetime.datetime.today()
    print(hora)

    if hora == "03:00:00":
        await channel.send(file = File("./Assets/videos_dia/macacoOleo.mp4"))

    if hora == "20:00:00":
        await channel.send(file = File("./Assets/videos_dia/dezessete.mp4"))

    #Segunda Feira
    if day.weekday() == 0 and hora == "15:00:00":
                embed = Embed(title = "SEGUNDA DA CAPIVARA",description = "CAPYBARA? CAPIVARA! COCONUT DOGGIE",colour = colour.Colour.blue())
                embed.set_image(url = "https://c.tenor.com/K3uxrqffdCAAAAAC/capybara-orange.gif")
                embed.set_footer(text= "Crias do Xamil", icon_url= "https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                await channel.send(embed = embed)
                await channel.send(file = File("./Assets/videos_dia/capivara.mp4"))
            
    #Terça
    if day.weekday() == 1 and hora == "15:00:00":
    
                        embed = Embed(title = "MAMACO FEIRA!",description = "UUUUUUUUUU AAAAAAA AAAAAAAAAAAA UUUUUU AAAAAAAA",colour = colour.Colour.dark_red())
                        embed.set_footer(text= "MAMACOS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_thumbnail(url="https://c.tenor.com/bB0vUlhGjygAAAAS/monkey-drinking.gif")
                        embed.set_image(url= "https://tenor.com/view/monkey-artificialbloom-monkey-hulahoop-monkey-dancing-gif-23688613")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/videos_dia/monkeTerca.mp4"))
            
    #Quarta
    if day.weekday() == 2 and hora == "15:00:00":
    
                        embed = Embed(title = "QUACK QUARTA!",description = "Quack!",colour = colour.Colour.dark_purple())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url = "https://tenor.com/view/duck-flower-hat-sunflower-gif-24583729")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/videos_dia/quackQuarta.mp4"))
    
    #Quinta

    if day.weekday() == 3 and hora == "15:00:00":
    
                        embed = Embed(title = "MUZY FEIRA",description = "DIA DE APRECIAR MÉDICO GOSTOSO QUE FAZ LIVE DE BICICLETINHA",colour = colour.Colour.dark_grey())
                        embed.set_thumbnail(url= "https://www.ignboards.com/attachments/tumblr_2085c7e9c94e11e100185eb9b2d5d13d_2e3c876b_250-gif.620178/")
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url = "https://www.ignboards.com/attachments/tumblr_7a022baa585c21ce3dedd71ea52c899c_b33912ab_400-gif.618089/")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/videos_dia/muzy.mp4"))
            

    #Sexta
    if day.weekday() == 4 and hora == "15:00:00":
    
                        embed = Embed(title = "SEXTA DOS CRIAS!",description = "SEXTA DOS CRIAS PORRA!",colour = colour.Colour.red())
                        embed.set_footer(text= "É OS CRIAS DO XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://c.tenor.com/J5O9kElWluYAAAAC/mucalol-smurfdomuca-muca-muquinha-dan%C3%A7ando-dan%C3%A7a-dancing-macaco-macacolol.gif")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/videos_dia/criaSexta.mp4"))
                        await channel.send(file = File("./Assets/videos_dia/shrekSexta.mp4"))
    
    

    #Sábado
    if day.weekday() == 5 and hora == "15:00:00":
        
                        embed = Embed(title = "SAUL SÁBADO",description = "Hi. I'm Saul Goodman. Did you know that you have rights? The Constitution says you do. And so do I. I believe that until proven guilty, every man, woman, and child in this country is innocent. And that's why I fight for you, Albuquerque! Better call Saul.",colour = colour.Colour.red())
                        embed.set_footer(text= "XAMIL",icon_url="https://cdn.discordapp.com/emojis/761013506384330752.png?v=1")
                        embed.set_image(url="https://tenor.com/view/afham-saul-goodman-better-call-saul-bob-odenkirk-jimmy-mcgill-gif-25559831s")
                        embed.set_thumbnail(url="https://tenor.com/view/better-ball-saul-better-call-saul-saul3d-saul-goodman3d-saul-ball-gif-25770284")
                        await channel.send(embed = embed)
                        await channel.send(file = File("./Assets/videos_dia/saul.mp4"))

@client.command()
async def rock(ctx):
    rand = random.randint(0,1)

    if rand == 0:
        await ctx.send(file = File("./Assets/videos_comandos/theRock.mp4"))

    if rand == 1:
        await ctx.send(file = File("./Assets/videos_comandos/theRock2.mp4"))

@client.command()
async def comedia(ctx):
    await ctx.send(file = File("./Assets/videos_comandos/MestreDaComedia.mp4")) 

@client.command()
async def omg(ctx):
    await ctx.send(file = File("./Assets/videos_comandos/omg.mp4"))   

@client.command()
async def sam(ctx):
    await ctx.send(file = File("./Assets/videos_comandos/there will be blood shed.mp4"))   

@client.command()
async def dmc(ctx):
    await ctx.send(file = File("./Assets/videos_comandos/vergil.mp4"))

@client.command()
async def standinghere(ctx):
    await ctx.send(file = File("./Assets/videos_comandos/bracoforte.mp4"))

@client.command()
async def fma(ctx):
    await ctx.send(file = File("./Assets/videos_comandos/fma.mp4"))

@client.command()
async def saul(ctx):
    rand = random.randint(0,1)

    if rand == 0:
        await ctx.send(file = File("./Assets/videos_comandos/saul 8bits.mp4"))

    if rand == 1:
        await ctx.send(file = File("./Assets/videos_comandos/Saul goodman 3d.mp4"))      

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
async def faro(ctx,chn = None):
        if(chn is not None):
            channel = client.get_channel(int(chn))
        else:
            channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        source = FFmpegPCMAudio('Assets/audios/faro.mp3')
        player = voice.play(source)
        while voice.is_playing():
            await sleep(1)
        await voice.disconnect() 


@client.command()
async def cavalo(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/cavalo.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def iha(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/iha.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def danca(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/danca.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def leite(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/muito-leite.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 



@client.command()
async def pare(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/pare.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def ph(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/ph.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def pressao(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/pressaoNenem.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def puta(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/puta.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def goofy(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/rodrigo-faro-sound.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def sla(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/sla.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def titio(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/titio.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def tome(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/tome.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def uepa(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/uepa.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def ui(ctx,chn = None):
    if (ctx.author.voice):
        if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/ui-rodrigo-faro.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def elegosta(ctx,chn = None):
    if(chn is not None):
        channel = client.get_channel(int(chn))
    else:
        channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/elegosta.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def queisso(ctx,chn = None):
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/que isso meu filho calma.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 

@client.command()
async def walter(ctx,chn = None):
    
    if(chn is not None):
            channel = client.get_channel(int(chn))
    else:
            channel = ctx.message.author.voice.channel
    voice = await channel.connect()
    source = FFmpegPCMAudio('Assets/audios/walter.mp3')
    player = voice.play(source)
    while voice.is_playing():
        await sleep(1)
    await voice.disconnect() 



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



client.run('ODgzMzI3OTUwMDgxMDk3NzI5.GA6gAu.QwALoCyxHzTr-Zol0hFCFHBEzNavA840uZQ4JQ')
