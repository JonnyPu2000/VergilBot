import discord
from discord.ext import commands
import datetime
import os
from time import sleep

client = commands.Bot(command_prefix = '.')
day = datetime.datetime.today()


@client.event
async def on_ready():
    print("Idosa Peladinha")
    channel = client.get_channel(645698417544265769)
    time = datetime.datetime.now().strftime("%H:%M")
    while time != "13:11":
        print(time)
        time = datetime.datetime.now().strftime("%H:%M")
        sleep(1)

    if day.weekday() == 4 and time == "13:11":
        await channel.send("https://www.youtube.com/watch?v=pCTSdupScwA")
        await channel.send("https://www.youtube.com/watch?v=8GX9--xhf_A")



client.run(os.environ['DISCORD_TOKEN'])