import discord

client = commands.Bot(command_prefix='&')

@client.event
async def on_ready():
    print("The bot is ready.")

client.run("ODA2NTgyMjMwODUxMTI1Mjkx.YBriPQ.iZhDsrK2fRzSEkmL4rM30gi4p8g")
