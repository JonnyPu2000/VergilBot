import discord
from discord.ext import commands
import datetime

client = commands.Bot(command_prefix = '.')
day = datetime.datetime.today()


@client.event
async def on_ready():
    channel = client.get_channel(645698417544265769)
    print("Penis de Idosa")
    time = datetime.datetime.now().strftime("%H:%M")
    while time != "11:02":
        time = datetime.datetime.now().strftime("%H:%M")
        print(time)
    if day.weekday() == 4 and time == "11:02":
        await channel.send("https://www.youtube.com/watch?v=pCTSdupScwA")
        await channel.send("https://www.youtube.com/watch?v=8GX9--xhf_A")



client.run('ODgzMzI3OTUwMDgxMDk3NzI5.YTIVQg.chXPKvfzqCtgR_aBHixu9FJl3Wg')