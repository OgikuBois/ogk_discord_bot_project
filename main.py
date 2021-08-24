from datetime import time
import discord
from discord import message
from discord.ext import commands,tasks
import os 
import tracemalloc
import json 
import youtube_dl
from youtube_dl import YoutubeDL
import discord.ext 
import math
import random
import casesinfo
from discord import FFmpegPCMAudio
import discord.utils
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd

riot_dev_api = "RGAPI-c84aa054-6d1f-4943-8604-a000551e68e2"


#client = discord.Client()

client = commands.Bot(command_prefix="$")

fd = open("bot_token.txt", "r")
bot_token = fd.read()

@client.event
async def on_ready(pass_context = True):
    print('Logged on as {0}!'.format(client))
#=======================================
#Text response
#========================================

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
#=======================================
#OWC
#========================================
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
async def IThinkItsTimeForOWC(ctx):
    await ctx.send("I think you're right!")


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
#=======================================
#Covid cases
#========================================
@client.command(pass_context = True)
async def covid(ctx):
    result = casesinfo.mainCases()
    await ctx.send("```" + result[0] +"\n" + result[1] + "```")
#=======================================
#Kings cup
#========================================
@client.command(pass_context = True)
async def kc(ctx):
    import kings_cup
    author=ctx.message.author.id
    authorName=str(ctx.message.author).split("#")
    
    validNumber=False
    await ctx.send("```" + "How many players do you have " + authorName[0] + "?" + "```")
    while validNumber==False:
        try: 
            message= await client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=10)
            try:
                noOfPlayers = int(message.content.strip())
                if noOfPlayers < 9 and noOfPlayers > 0:
                    validNumber=True
                else: 
                    await ctx.send("``` Error: Please enter number between 1-8 ```")
            except ValueError: 
                await ctx.send("``` Error: Please enter number between 1-8 ```")
        except asyncio.TimeoutError:
                await ctx.channel.send("No input :(")
                break
    if validNumber:
        playerList = []
        while len(playerList) != noOfPlayers:
            await ctx.send("```" + "Enter a player's name " + "```")
            try:
                message= await client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=10)
                try: 
                    if isinstance(message.content, str):
                        playerList.append(message.content)
                except ValueError:
                    await ctx.send("```Error: enter valid name```")
            except asyncio.TimeoutError:
                    await ctx.channel.send("No input :(")
        kcReturn=kings_cup.main(playerList)
        msg_output=""
        for i in kcReturn:
            msg_output+="Player: " + str(i[0].capitalize()) + " has traits " + str(i[1]) +" and " + str(i[2]) +", and has a king of " + str(i[3]) + "\n"
        await ctx.send("```prolog\n" + msg_output +"```")

# def check(origAuth, newAuth):
#     print("Original Author: {} \nNew Author: {}".format(origAuth,newAuth))
#     return origAuth == newAuth


#=======================================
#Music Bot
#========================================
ffmpeg_options = {
    'options': '-vn'
}

ytdl_format_options = {
'format': 'bestaudio',
'postprocessors': [{
    'key': 'FFmpegExtractAudio',
    'preferredcodec': 'mp3',
    'preferredquality': '192',
}],
'outtmpl': 'song.%(ext)s',
}
ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)
class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = ""
    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = data['title'] if stream else ytdl.prepare_filename(data)
        return filename




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
async def play(ctx, url):
    try:
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            filename = await YTDLSource.from_url(url, loop=client.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        await ctx.send('**Now playing:** {}'.format(filename))
    except:
            await ctx.send("The bot is not connected to a voice channel.")

@client.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")
    
@client.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        await voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

@client.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.stop()
    else:
        await ctx.send("The bot is not playing anything at the moment.")



"""
================
Cilent
================
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

"""


client.run(bot_token)

