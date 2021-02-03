import discord
from discord.ext import commands

client = commands.Bot(command_prefix='&')

timeout =  36000

@client.event
async def on_ready():
    print("The bot is ready.")

@client.command(pass_context=True)
async def message(ctx):
    await ctx.message.send("ciao")

client.run("ODA2NTgyMjMwODUxMTI1Mjkx.YBriPQ.iZhDsrK2fRzSEkmL4rM30gi4p8g")
