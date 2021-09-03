import discord
from discord.ext import commands
import datetime
import os
import time as tm

client = commands.Bot(command_prefix = '.')
day = datetime.datetime.today()
time = datetime.datetime.now().strftime("%H:%M")


@client.event
async def on_ready():
    print("Idosa Peladinha")
    channel = client.get_channel(645698417544265769)
    time = datetime.datetime.now().strftime("%H:%M")

    for i in range(0,60):
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
        if time == "13:07":
            print("FOI")
            break
        tm.sleep(5)
    print("SAIU") 

    if day.weekday() == 4 and time == "13:08":
        print("ENTROU")
        await channel.send("https://www.youtube.com/watch?v=pCTSdupScwA")
        await channel.send("https://www.youtube.com/watch?v=8GX9--xhf_A")



client.run(os.environ['DISCORD_TOKEN'])