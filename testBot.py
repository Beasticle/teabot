import discord
from discord import channel, message
from discord.ext import commands
import time

from discord.ext.commands.bot import Bot

client = commands.Bot(command_prefix= '$')

currentHr = time.strftime("%H")
teaCount = 0
teaType = []

@client.event
async def on_ready():
    print('Bot is ready.')

    
@client.event
async def on_message(message):
    if message.content.startswith('$addCup'):
        channel = message.channel
        await channel.send('what tea did you drink?')

        def check(m):
            global msg2
            msg2 = m.content
            return m.content.startswith('I drank')
        
        chk = await client.wait_for('message', check=check)
        await channel.send('Added your cup to the list!' .format(chk))
        
        msgList = str(msg2).split('drank ')
        teaCount =+ 1
        print(msgList)
        msg = str(msgList[1])
        teaType.append(msg)
        print(teaCount, teaType, currentHr)
 
@client.command()
async def test(ctx):
    await ctx.send("Test Complete") 
       
async def backgroundTask():
    if currentHr == "00":
        teaCount = 0
        teaType = []


client.loop.create_task(backgroundTask())
client.run("Change this")
