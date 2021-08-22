import discord
from discord.ext import commands,tasks
import os 
import tracemalloc
import json 
import youtube_dl
import discord.ext 
import math
import random
from casesinfo import *


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
async def gay(ctx):
    await ctx.send("```{} is gay```".format(ctx.message.author))

@client.command(pass_context = True)
async def ayy(ctx):
    await ctx.send("lmao")

@client.command(pass_context = True)
async def owc(ctx):
    await ctx.send("owcComplete, owcList, owcClear")

@client.command(pass_context = True)
async def pp(ctx):
    ppSize = random.randrange(1,16)
    await ctx.send("{}".format(ctx.message.author) + " pp: 8" + "=" * ppSize + "D")

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
async def owcComplete(ctx, owcMap):
    ofd = open("new_owc.txt", "r+")
    wfd = open("temp_owc.txt", "w+")
    for x in ofd:
        output = ""
        line = x.split('\n')
        nl = line[0].split(':')
        if nl[0] == str(owcMap):
            nl = ["= ", nl[0], ":", nl[1], " ="]
        else:
            if len(nl)>1:
                nl = [nl[0], ":", nl[1]]
        for i in nl:
            output += i
        output += "\n"
        wfd.write(output)

    ofd.close()
    wfd.close()

    with open("temp_owc.txt") as f:
        with open("new_owc.txt", "w") as f1:
            for line in f:
                f1.write(line)
    os.remove("temp_owc.txt")
#send
    rfd = open("new_owc.txt", "r")
    await ctx.message.channel.send(rfd.read())

@client.command(pass_context = True)
async def owcList(ctx):
    rfd = open("new_owc.txt", "r")
    await ctx.send(rfd.read())

@client.command(pass_context = True)
async def owcClear(ctx):
    with open("new_owc.txt") as f:
        with open("temp_owc.txt", "w") as f1:
            for x in f:
                line = x.replace("=", "")
                if line[0] == " ":
                    line = line.strip()
                    line += "\n"
                f1.write(line)
                  
    with open("temp_owc.txt") as f:
        with open("new_owc.txt", "w") as f1:
            for line in f:
                f1.write(line)

    os.remove("temp_owc.txt")
    rfd = open("new_owc.txt", "r")
    await ctx.send(rfd.read())
#===================
@client.command(pass_context = True)
async def play(ctx, song):
    await ctx.send("!play " + song)

#========================
@client.command(pass_context = True)
async def covid(ctx):
    await ctx.send("```" + result + "```")


#================
#Cilent
#================
# @client.event
# async def on_message(message):
#     print('Message from {0.author}: {0.content} in channel: {0.channel}'.format(message))
#     message.content = message.content.lower()

#     if "ayy" in message.content.lower():
#         storedMessage = message.content.lower()
#         lmaoCounter = 0
#         counter = 0
#         for i in storedMessage:
#             counter += 1
#             if counter + 2 <= len(storedMessage):
#                 if storedMessage[counter] == "a" and storedMessage[counter + 1] == "y" and storedMessage[counter + 2] == "y":
#                     lmaoCounter = len(storedMessage) - 2 - counter 
                   
#         await message.channel.send("lmao" + "o" * lmaoCounter)
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

