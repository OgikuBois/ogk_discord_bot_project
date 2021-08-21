import discord
from discord.ext import commands,tasks
import os 
import tracemalloc
import json 
import youtube_dl
import discord.ext 


riot_dev_api = "RGAPI-c84aa054-6d1f-4943-8604-a000551e68e2"


#client = discord.Client()


client = commands.Bot(command_prefix="$")

fd = open("bot_token.txt", "r")
bot_token = fd.read()

@client.event
async def on_ready(pass_context = True):
    print('Logged on as {0}!'.format(client))


@client.command(pass_context = True)
async def commands(ctx):
    await ctx.message.channel.send("```$hello | Displays a hello message.\n$play `{YouTube link or video name`} | Plays a provided song\n```")


@client.command(pass_context = True)
async def hello(ctx):
    await ctx.send("```Hello {}```".format(ctx.message.author))

@client.command(pass_context = True)
async def bad(ctx):
    await ctx.send("```No you```")

@client.command(pass_context = True)
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.message.author.voice.channel
        await channel.connect()
    else:
        ctx.send("```Please join a voice channel to user this command.```")

@client.command(pass_context = True)
async def dc(ctx):
    if ctx.voice_client:

        await ctx.guild.voice_client.disconnect()
        await ctx.send("```Cya.```")

    else:
        await ctx.send("```I'm not in the call.```")

@client.command(pass_context = True)
async def owc(ctx):
    await ctx.message.channel.send("```asciidoc\nSCORE V2 + NF\n\n[Long Maps]\nLM1: Boku ga Namae o Yobu Hi feat.Mochizuki Souta (5:02 mins) 5.43* 1213586\nLM2: Image Material 5.58* (6:50 mins) 1408632\nLM3: Yomi Yori  5.76* (8:10 mins) 2190486\n\n[No Mod]\nNM1: Nini (Burst map) 5.71* 1953873\nNM2: Freedom dive Metal dimensions 5.77* 1915983\nNM3: Mizuoto to curtain 5.89* 2025942\nNM4: Last Goodbye 6.46* 1570203\nNM5: Airman 7.08* 104229\n\n[Double Time]\nDT1: Doraemon 4.46* 1814702\nDT2: Let it snow 5.41* 1153526\nDT3: Yuki no Hana 6.23* 968350\n\n[Relax]\nRX1: Mou ii kai 6.87* 1695382\nRX2: Road of resistance 7.33* 869222\nRX3: Goodbye 8.36* 1172819\n\n[Hidden]\nHD1: Seventeen RPG 4.98* 719443\nHD2: Amazing Break 5.47* 1217004\nHD3: Colorful 6.00* 1947084\n\n[Free Mod]\nFM1: Chika Chika 5.39* 1970829\nFM2: Ai no sukima 5.74* 1988753\nFM3: Yubi bouenkyou 5.80* 1474956\n```\n")

@client.command(pass_context = True)
async def owcFormat(ctx ):



"""
@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content} in channel: {0.channel}'.format(message))
    message.content = message.content.lower()

    if "ayy" in message.content.lower():
        storedMessage = message.content.lower()
        lmaoCounter = 0
        counter = 0
        for i in storedMessage:
            counter += 1
            if counter + 2 <= len(storedMessage):
                if storedMessage[counter] == "a" and storedMessage[counter + 1] == "y" and storedMessage[counter + 2] == "y":
                    lmaoCounter = len(storedMessage) - 2 - counter 
                   
        await message.channel.send("lmao" + "o" * lmaoCounter)


    if message.content.startswith("$play"):
        song = ""
        messageContent = message.content.strip().split(" ")
        for i in range(1, len(messageContent)):
            song += messageContent[i] + " "
        await message.channel.send("!play" + " " + song)
"""
def kings_cup(player_list):
    pass


client.run(bot_token)

