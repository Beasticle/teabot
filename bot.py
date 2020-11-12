import discord
from discord import activity
from discord.emoji import Emoji
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
    while True:
        if teaCount < 2:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Julian sip tea"))
        elif 2 < teaCount < 4:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Julian drink tea"))
        elif 4 < teaCount:
            await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Julian chug tea"))
            
    await client.process_commands(message)

@client.command()
async def test(ctx):
    await ctx.send("Test Complete") 
    
@client.command()
async def teaCups(ctx):
    await ctx.send(f'Julian has drank {teaCount} cups of tea')
    
@client.command()
async def typeOfTea(ctx):
    await ctx.send(f'Julian has drank {teaType} tea.')

@client.event
async def on_message(message):
    global teaCount, teaType
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
        teaCount += 1
        #print(msgList)
        msg = str(msgList[1])
        teaType.append(msg)
        print(teaCount, teaType, currentHr)
        
    await client.process_commands(message)
       
async def backgroundTask():
    global teaCount
    if currentHr == "00":
        teaCount = 0
        teaType = []


client.loop.create_task(backgroundTask())
client.run("Nzc2MTc2NTc2MzAyODA5MTM5.X6xExA.UQshF_nnF8CfsasgfMjNCw4iLtQ")