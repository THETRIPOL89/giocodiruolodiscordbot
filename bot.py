import discord
from discord.ext import commands

client = commands.Bot(command_prefix='&')

timeout =  36000

@client.event
async def on_ready():
    print("The bot is ready.")
    channel = client.get_channel(706775759615950908)
    while True:
        await channel.send("!add-money-role cash <@805495893766963201> 100")
        await asyncio.sleep(timeout)

client.run("ODA2NTgyMjMwODUxMTI1Mjkx.YBriPQ.iZhDsrK2fRzSEkmL4rM30gi4p8g")
