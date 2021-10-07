from datetime import time
import discord
from discord import message
from discord import reaction
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
import pytz
from discord import FFmpegPCMAudio
import discord.utils 
import asyncio
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pandas as pd
from discord_components import DiscordComponents, Button, ButtonStyle, ComponentsBot, Select, SelectOption
from sys import exit
#pip install --upgrade discord-components

riot_dev_api = "RGAPI-c84aa054-6d1f-4943-8604-a000551e68e2"


#client = discord.Client()

client = commands.Bot(command_prefix="$")

# fd = open("bot_token.txt", "r")
# bot_token = fd.read()

try:  
   bot_token=os.environ["bot_token"]
except KeyError: 
   print("Please set the environment variable bot_token")
   exit(1)

@client.event
async def on_ready(pass_context = True):
    print('Logged on as {0}!'.format(client))
#=======================================
#Text response
#========================================

@client.command(pass_context = True)
async def commands(ctx):
    await ctx.message.channel.send("```$hello | Displays a hello message.\n$play `{Yo   uTube link or video name`} | Plays a provided song\n```")

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
async def ayyConstant(ctx):
    print("ayyConstant is on")
    await ctx.message.delete()
    isItTrue = True
    lenStore = 1
    
    while isItTrue:
        message = await client.wait_for('message')
        channel = message.channel
        authorName = str(message.author).split("#")[0]
        try:
            messageStore = str(message.content).lower().split(" ")
        except:
            messageStore = str(message.content).lower()
        if any("ayy" in s for s in messageStore):
            print(authorName + ":")
            print(messageStore) 
            for i in range(len(messageStore)):
                messageStoreI = messageStore[i]
                for j in range(len(messageStoreI)):
                    if j + 2 < len(messageStoreI):
                        if messageStoreI[j] == "a" and messageStoreI[j + 1 ] == "y" and messageStoreI[j + 2] == "y":
                            lenStore = len(messageStoreI) - j - 3
            await channel.send("lmao" + lenStore * "o")


@client.command(pass_context = True)
async def owc(ctx):
    await ctx.send("owcComplete, owcList, owcClear")


@client.command(pass_context = True)
async def me(ctx, *, extra):
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")[0]
    await ctx.message.delete()
    await ctx.send("```\n" + authorName + " " + extra + "```")

@client.command(pass_context = True)
async def spam(ctx, *, extra):
    await ctx.message.delete()
    for i in range(0,11):
        botMessage = await ctx.send("Where are you " + extra)
        await botMessage.delete()

@client.command(pass_context = True)
async def nCheck(ctx):
    doItToEm = 0
    testItToEm = 0
    await ctx.message.delete()
    isItTrue = True
    while isItTrue:
        message = await client.wait_for('message')
        authorName = str(message.author)
        authorName = authorName.split("#")[0]
        channel = message.channel
        print(authorName + ": " + str(message.content).strip().lower())
        if str(message.content).strip().lower() == "nigger" or str(message.content).strip().lower() == "nigga" or str(message.content).strip().lower() == "niga":
            doItToEm = 1
        if str(message.content).strip().lower() == "test":
            testItToEm = 1
        if str(message.content).strip().lower() == "end":
            isItTrue = False
        if doItToEm == 1:
            for i in range(0,5):
                await channel.send(authorName + " said the N word!1!!1!1!111!!!")
                doItToEm = 0
        if testItToEm == 1:
            for i in range(0,5):
                await channel.send(authorName + " is testing the n word check.")
                testItToEm = 0


@client.command(pass_context = True)
async def nFix(ctx):
    await ctx.message.delete()
    print("nFix is on")
    fixIt = 0
    nWordVariants = ["nigga", "nigger", "niggas", "niggers", "n4gga", "n4ggas", "negus", "n1gger", "n1ggers"]
    iStore = 0
    while True:
        output = ""
        message = await client.wait_for('message')
        authorName = str(message.author)
        authorName = authorName.split("#")[0]
        channel = message.channel
        messageStore = str(message.content).strip().lower().split(" ")
        for j in nWordVariants:
            if any(j in s for s in messageStore):
                print(authorName + ":")
                print(messageStore)
                fixIt = 1
                for i in range(len(messageStore)):
                    # if any(j in s for s in messageStore[i]):
                    if messageStore[i] == j:
                        iStore = i
                        
        if fixIt == 1:
            await message.delete()
            messageStore[iStore] = "Kanye"
            for i in range(len(messageStore)):
                output += str(messageStore[i]) + " "
            await channel.send("What " + authorName + " was meant to say was: " + output)
            fixIt = 0


@client.command(pass_context = True)
async def roll(ctx):
    rngRoll = random.randrange(0,101)
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")[0]
    await ctx.send(authorName + " rolled: " + str(rngRoll))

@client.command(pass_context = True)
async def coin(ctx):
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")[0]
    rngCoin = random.randrange(0,2)
    if rngCoin == 0:
        output = "Heads"
    if rngCoin == 1:
        output = "Tails"
    await ctx.send(authorName + " flipped a: " + output)

@client.command(pass_context = True)
async def beef(ctx, *, badPerson):
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")
    authorName = authorName[0]
    badPerson = str(badPerson)
    with open("beef.txt", "a") as fd:
        fileInput = authorName.capitalize() + " has beef with: " + badPerson.capitalize()
        fd.writelines(fileInput + "\n")
        await ctx.send("```Done.```")
    await beefList(ctx)

@client.command(pass_context = True)
async def beefList(ctx):
    messageOutput = ""
    with open("beef.txt", "r") as fd:
        messageOutput = fd.read()
        await ctx.send("```prolog" + "\n" + messageOutput + "```")

@client.command(pass_context = True)
async def beefRemove(ctx, *, badPerson):
    messageOutput = ""
    removalLine = 0
    lineCounter = 0
    badPersonStore = str(badPerson)
    badPersonStore = badPersonStore
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")
    authorName = authorName[0]
    removeCheck = False

    try:
        authorName = authorName.split(" ")
        authorName = authorName[0]
    except:
        pass
 
    with open("beef.txt", "r+") as fd:
        lines = fd.readlines()
        linesList = []
        for line in lines:  
            lineCounter += 1
            linesList.append(line)
            lastWord = line.split(": ")
            firstWord = lastWord[0].split(" ")
            firstWord = firstWord[0]
            lastWord = lastWord[-1].strip()
            print(authorName.capitalize(), firstWord, badPersonStore.capitalize(), lastWord)

            if authorName.capitalize() == firstWord and badPersonStore.capitalize() == lastWord:
                print("True")
                await ctx.send("``` Done. ```")
                removalLine = lineCounter
                removeCheck = True
            else:
                print("False")

        print("Before: " + str(linesList))

        if removeCheck == False:
            await ctx.send("```Person's name was not recognised. Type the name at the end.```")

        if removeCheck == True:
            del linesList[removalLine - 1]
        
        print("After: " + str(linesList))

        for i in range(len(linesList)):
            messageOutput += str(linesList[i])
    with open("beef.txt", "w+") as fd:
        fd.write(messageOutput)
    await beefList(ctx)

@client.command(pass_context = True)   
async def pp(ctx):
    ppSize = random.randrange(1,16)
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")
    authorName = authorName[0]
    if authorName == "Cryogenics":
        await ctx.send("Cryogenics pp: 8" + "======================================================================" * ppSize + "D")
    else:
        await ctx.send("{}".format(authorName) + " pp: 8" + "=" * ppSize + "D")

@client.command(pass_context = True)   
async def shutUp(ctx):
    beQuiet = True
    authorName = ctx.message.author
    print(str(authorName) + " called for shut up.")
    print("I am ready to shut someone up.")
    await ctx.message.delete()
    message = await client.wait_for('message')
    channel = message.channel
    print("Currently shutting this person up: "+ str(message.author))
    await channel.send("Shut up. I dare ya to speak gouma.")
    print("Currently doing them dirty.")
    while beQuiet:
        try:
            message = await client.wait_for('message', check=lambda m: m.author == message.author, timeout = 15)
            channel = message.channel
            await channel.send("Why you still talking?")
        except asyncio.TimeoutError:
            await channel.send("You may now speak ya gronk.")
            beQuiet = False
            break

@client.command(pass_context = True)   
async def shadowRealm(ctx, *, ripPerson):
    await ctx.message.delete()
    print(str(ctx.message.author) + ": $shadowRealm " + ripPerson)
    await ctx.send(ripPerson + ". You have been sent to the shadow realm.")
    inTheShadowRealm = True
    messageOutput = "Banned person: " + str(ripPerson) + "\n"

    while inTheShadowRealm:
        try:
            message = await client.wait_for('message', timeout = 30)
            channel = message.channel
            messageAuthor = str(message.author).split("#")[0]
            if messageAuthor.strip() == ripPerson.strip():
                await message.delete()
                print(messageAuthor + " deleted message: " + message.content)
                messageOutput += "Deleted message: " + message.content + "\n"
                await channel.send("bruh why you trying to talk fam? You in the shadow realm.")
        except asyncio.TimeoutError:
            await channel.send("You free now.")
            inTheShadowRealm = False
            break
        
    if inTheShadowRealm == False:
        with open("shadowRealmLogs.txt", "a") as fd:
            fd.writelines(messageOutput)
            
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

@client.command(pass_context = True)
async def genshinUpdate(ctx, *, whichLine):
    messageOutput = ""
    times = 1
    lineCounter = -1
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")[0]
    finisher = ""
    doYourThing = False
    lineStoreSecond = ""
    if whichLine == "1" or whichLine == "3" or whichLine == "5":
        await ctx.send("```What is the updated number?```")
        if whichLine == "1":
            finisher = "/90"
        elif whichLine == "3":
            finisher = "/80"      
    
    elif whichLine == "2" or whichLine  == "4":
        await ctx.send("Done.")
    elif whichLine == "all":
        times = 5
    else: 
        await ctx.send("```Invalid input.```")

    with open("genshinPulls.txt", "r+") as fd:
        lines = fd.readlines()
        for line in lines:
            lineCounter += 1
            lineStore = line
            lineStoreFirst = lineStore.split(":")[0]
            try:
                lineStoreSecond = lineStore.split(":")[1] 
            except:
                pass
        
            if line[0] == "[":
                nameChecker = line.split("[")[1].split("]")[0]
      
            if authorName.strip() == nameChecker.strip():
                doYourThing = True
                lineCounter = 0
                nameChecker = ""

            if doYourThing == True:
                if whichLine == str(lineCounter):
                    if lineCounter == 2 or lineCounter == 4:
                        if lineStoreSecond.strip() == "False":
                            lineStoreSecond = "True\n"
                        else:
                            lineStoreSecond = "False\n"
                        lineStore = lineStoreFirst + ": " + lineStoreSecond

                    else:
                        try:
                            print("Genshin Update: Waiting.")
                            message = await client.wait_for('message', check=lambda m: m.author == ctx.author, timeout = 120)
    
                        except asyncio.TimeoutError:
                            await ctx.send("```bruh you took too long to type something.```")
        
        
                        if lineCounter == 5:
                            quickMaths = float(message.content) / 160
                            lineStore = lineStoreFirst + ": " + str(message.content) + " (" + str(quickMaths) + " summons)" + "\n"
        
                        else:
                            lineStore = lineStoreFirst + ": " + str(message.content) + finisher + "\n"
                else: 
                    lineStore = lineStoreFirst + ": " + lineStoreSecond
                    if lineCounter == 0:
                        lineStore = lineStoreFirst

                messageOutput += lineStore


            if doYourThing == False:
                messageOutput += lineStore
            if lineCounter == 5:
                doYourThing = False
 
    with open("genshinPulls.txt", "w+") as fd:
        fd.writelines(messageOutput)
    await genshinStats(ctx)

@client.command(pass_context = True)
async def genshinStats(ctx):
    channel = ctx.message.channel
    with open("genshinPulls.txt", "r") as fd:
        messageOutput = fd.read()   
        botMessage = await channel.send("```prolog" + "\n" + messageOutput + "```")
        await asyncio.sleep(10)
        await botMessage.delete()

@client.command(pass_context = True, help = "$GenshinUpdate <line number>, add the line you want to update afterwards, e.g. $genshinUpdate 1.")
async def genshinList(ctx):
    channel = ctx.message.channel
    with open("genshinPulls.txt", "r") as fd:
        messageOutput = fd.read()
        botMessage = await channel.send("```prolog" + "\n" + messageOutput + "```")
        # await asyncio.sleep(10)
        # await botMessage.delete()
    


    # timeToSleep = True
    # if timeToSleep == True:
    #     print("bout to sleep")
    #     time.sleep(10)
    #     print("about to delete")
    #     await botMessage.delete()
    #     timeToSleep = False

@client.command(pass_context = True)
async def genshinPrimos(ctx, *, primosAdded):
    with open("genshinPulls.txt", "r+") as fd:
        lines = fd.readlines()
        currentPrimos = 0
        messageOutput = ""
        for line in lines:
            lineStore = line
            if lineStore[0] == "5":
                lineStoreFirst = lineStore.split(":")[0]
                currentPrimos = lineStore.split(":")[1].split("(")[0]
                currentPrimos = int(currentPrimos.strip())
                currentPrimos = currentPrimos + int(primosAdded)
                quickMaths = float(currentPrimos) /160
                lineStore = lineStoreFirst + ": " + str(currentPrimos) + " (" + str(quickMaths) + " summons)\n"
            messageOutput += lineStore

    with open("genshinPulls.txt", "w+") as fd:
        fd.writelines(messageOutput)
    
    await genshinStats(ctx)






@client.command(pass_context = True)
async def genshinAdd(ctx):
    authorName = str(ctx.message.author)
    authorName = authorName.split("#")[0]
    messageOutput = ""
    answered1 = True
    answered2 = True

    with open("genshinPulls.txt", "a") as fd:
        messageOutput += "[" + authorName + "]\n"
        await ctx.send("```What is your character banner pity?```")
        message = await client.wait_for('message', check=lambda m: m.author == ctx.author)
        messageOutput += "1. character: " + str(message.content) + "/90\n"
    
        while answered1:
            await ctx.send("```Are you guaranteed a character? Answer True/False.```")
            message = await client.wait_for('message', check=lambda m: m.author == ctx.author)
            if str(message.content) == "True" or str(message.content) == "False":
                messageOutput += "2. guaranteed character: " + str(message.content) + "\n"
                answered1 = False
                break
            else:
                await ctx.send("```Invalid input. Answer with either True/False.```")
        
        await ctx.send("```What is your weapon banner pity?```")
        message = await client.wait_for('message', check=lambda m: m.author == ctx.author)
        messageOutput += "3. weapon: " + str(message.content) + "/80\n"

        while answered2:
            await ctx.send("```Are you guaranteed a weapon? Answer True/False.```")
            message = await client.wait_for('message', check=lambda m: m.author == ctx.author)
            if str(message.content) == "True" or str(message.content) == "False":
                messageOutput += "4. guaranteed weapon: " + str(message.content) + "\n"
                answered1 = False
                break
            else:
                await ctx.send("```Invalid input. Answer with either True/False.```")

        await ctx.send("```How many primos do you have right now?```")
        message = await client.wait_for('message', check=lambda m: m.author == ctx.author)
        quickMaths = float(message.content) / 160
        messageOutput += "5. current primos: " + str(message.content) + " (" + str(quickMaths) + " summons)\n"

        fd.writelines(messageOutput)
        await ctx.send("```Done.```")

    await genshinStats(ctx)

#===========================
#Ready up check
#===========================
# @client.command(pass_context = True)
# async def ready(ctx, game):
#     players = []
#     aaaaaa = game
#     messageOutput = ""
#     authorName = str(ctx.message.author).split("#")
#     messageOutput += authorName[0]
#     messageOutput = ("```prolog\n" + messageOutput + "```")
#     await ctx.send(
#         messageOutput,
#         components = [
#             [Button(label = "Ready Up", custom_id = "readyUpButton"), Button(label = "Unready", custom_id = "unreadyButton")]
#         ]
#     )
#     interaction = await client.wait_for("button_click", check = lambda i: i.custom_id == "readyUpButton")
#     await interaction.respond(content = "Button clicked!")

on_command = 0
@client.command(pass_context = True, help='Type $ready, then enter @<game> with an optional note')
async def ready(ctx):
    channel = ctx.message.channel
    await ctx.message.delete()
    botReadyMessage = await channel.send("```I am ready. Tag a game and optionally write a note. For example: @Valorant quick we are starting in 2 minutes.```")
    playersListComing = []
    playersListNotComing = []
    playersListLater = []
    messageOutput = ""
    readyUpButton = client.get_emoji(746348476241150023)
    unreadyButton = client.get_emoji(283894246380142602)
    # reactionEmojis = [":bwabwey:746348476241150023", ":SamSleeper:743015860662304808"]
    reactionEmojis = ["✅", "🕐", "❌"]
    reactionSpecialEmojis = ["✅", "🕐", "❌", "🍆", "💦", ":SamSleeper:743015860662304808"]
    gameID = ""
    extra = ""
    message = ""
    # gameName = ""
    # oldGameID = ""
    playerCounterComing = 1
    playerCounterNotComing = 1
    playerCounterLater = 1
    delayCheck = False

#+ f"{readyUpButton}"
    authorName = str(ctx.message.author).split("#")
    def reactionCheck(reaction, user):
        return user and str(
            reaction.emoji) in reactionEmojis

    # if game.lower() == "val" or game.lower() == "valorant":
    #         gameID = "<@&752119026200739900>"
    # messageOutput +=  gameID + "\n"
    # global on_command
    # if on_command == 1:
    #     await ctx.send("I am already ready")
    #     return
    on_command = 1
    # while on_command == 1:
    oops = True
    while oops:
        try:
            message = await client.wait_for('message', check=lambda m: m.author == ctx.author, timeout=60)
        except asyncio.TimeoutError:
            await ctx.send("```bruh you took too long to type something.```")
        channel = ctx.message.channel
        messageContentFirst = message.content.split(" ")
        extra = messageContentFirst[1:]
        messageContentFirst = messageContentFirst[0]
        print(messageContentFirst)
        await botReadyMessage.delete()
        await message.delete()
    #games list
        gameIDList = ["<@&752119026200739900>", "<@&754996624761290793>", "<@&879892248496603148>", "<@&753916061161619486>", "<@&767208151614619698>", "<@&775135405099974706>", "<@&833563762514460672>", "<@&866222623448498188>", "<@&869413400948654120>", "<@&874885896057540669>", "<@&872801512768823326>", "pico"  ]
        gameNameList = ["Valorant", "League Of Legends", "Osu", "Movie Night", "Phasmophobia", "Apex Legends", "Maplestory", "Dota", "Genshin Impact", "CSGO", "Prop Hunt", "Pico Park"]
        for i in range(len(gameIDList)):
            if messageContentFirst == gameIDList[i]:
                gameID = gameIDList[i] #I know this is redundant, but I want to make it very clear and obvious.
                gameName = gameNameList[i]

        """
        if messageContentFirst == "<@&752119026200739900>":
            gameID = "<@&752119026200739900>"
            gameName = "Valorant"
        if messageContentFirst == "<@&754996624761290793>":
            gameID = "<@&754996624761290793>"
            gameName = "League Of Legends"
        if messageContentFirst == "<@&879892248496603148>":
            gameID = "<@&879892248496603148>"
            gameName = "Osu"
        if messageContentFirst == "<@&753916061161619486>":
            gameID = "<@&753916061161619486>"
            gameName = "Movie Night"
        if messageContentFirst == "<@&767208151614619698>":
            gameID = "<@&767208151614619698>"
            gameName = "Phasmophobia"
        if messageContentFirst == "<@&775135405099974706>":
            gameID = "<@&775135405099974706>"
            gameName = "Apex Legends"
        if messageContentFirst == "<@&833563762514460672>":
            gameID = "<@&833563762514460672>"
            gameName = "Maplestory"
        if messageContentFirst == "<@&866222623448498188>":
            gameID = "<@&866222623448498188>"
            gameName = "Dota"
        if messageContentFirst == "<@&869413400948654120>":
            gameID = "<@&869413400948654120>"
            gameName = "Genshin Impact"
        if messageContentFirst == "<@&874885896057540669>":
            gameID = "<@&874885896057540669>"
            gameName = "CSGO"
        if messageContentFirst == "<@&872801512768823326>":
            gameID = "<@&872801512768823326>"
            gameName = "Prop Hunt"
        """
    #send function
        if gameID != "":
            await ctx.send(gameID)
            messageOutput = (
                authorName[0].capitalize() + " has started a ready check for: " + gameName + " | additional notes: ")
        
            for i in extra:
                try:
                    i = i.capitalize()
                except:
                    pass
                messageOutput += i + " "

            messageOutput += ("\n" + "players ready:" + "\n")
            for i in playersListComing:
                messageOutput += str(playerCounterComing) + ". " + i.capitalize() + "\n"
                playerCounterComing += 1

            messageOutput += ("players coming next game:" + "\n")
            for i in playersListLater:
                messageOutput += str(playerCounterLater) + ". " + i.capitalize() + "\n"
                playerCounterLater += 1

            messageOutput += "players not coming:" + "\n"

            for i in playersListNotComing:
                messageOutput += str(playerCounterNotComing) + ". " + i.capitalize() + "\n"
                playerCounterNotComing += 1

            messageOutput += "total number of players ready: " + str(playerCounterComing - 1)
            messageOutput += "\n"
            messageOutput += "total number of players not coming: " + str(playerCounterNotComing - 1)     
            messageOutput = ("\n" + "```prolog" + "\n" + messageOutput + "```")

            botMessage = await channel.send(messageOutput)
            easterEggRNG = random.randrange(0,11)
            if easterEggRNG == 10:
                for i in range(len(reactionSpecialEmojis)):
                    await botMessage.add_reaction(reactionSpecialEmojis[i])
            else:   
                for i in range(len(reactionEmojis)):
                    await botMessage.add_reaction(reactionEmojis[i])
            oldGameID = gameID
            gameID = ""
            delayCheck = True
            
#add reaction interaction
        playersListComing.append(authorName[0])
        updateList = 1
        while delayCheck:
            #List updater
            if updateList == 1:
                updateList = 0
                try: 
                    playersListNotComing.remove("Ogikubot")
                except:
                    pass
                for i in range(len(playersListNotComing)):
                    if playersListNotComing[i] == "Ogikubot":
                        del playersListNotComing[i]

                messageOutput = (
                    authorName[0].capitalize() + " has started a ready check for: " + gameName + " | additional notes: ")
            
                for i in extra:
                    try:
                        i = i.capitalize()
                    except:
                        pass
                    messageOutput += i + " "
                messageOutput += ("\n" + "players ready:" + "\n")
                for i in playersListComing:
                    messageOutput += str(playerCounterComing) + ". " + i.capitalize() + "\n"
                    playerCounterComing += 1
                    # botMessage = await ctx.send(gameID + "\n" + "```prolog" + "\n" + messageOutput + "```")

                messageOutput += ("players coming next game:" + "\n")
                for i in playersListLater:
                    messageOutput += str(playerCounterLater) + ". " + i.capitalize() + "\n"
                    playerCounterLater += 1

                messageOutput += "players not coming:" + "\n"

                for i in playersListNotComing:
                    messageOutput += str(playerCounterNotComing) + ". " + i.capitalize() + "\n"
                    playerCounterNotComing += 1
                messageOutput += "total number of players ready: " + str(playerCounterComing - 1)
                messageOutput += "\n"
                messageOutput += "total number of players not coming: " + str(playerCounterNotComing - 1)            
                messageOutput = ("\n" + "```prolog" + "\n" + messageOutput + "```")
                await botMessage.edit(messageOutput)           

            try:
                reaction, user = await client.wait_for('reaction_add', check = reactionCheck, timeout = 60 * 5)
                if user != "OgikuBot#3742":
                    if str(reaction.emoji) == "✅":
                        playerCounterComing = 1
                        playerCounterNotComing = 1
                        playerCounterLater = 1
                        username = str(user)
                        username = username.split("#")
                        username = username[0]
                        updateList = 1   
                        if any(username in s for s in playersListComing):
                            pass
                        else:
                            playersListComing.append(username)

                        if any(username in s for s in playersListNotComing):
                            playersListNotComing.remove(username)
                        if any(username in s for s in playersListLater):
                            playersListLater.remove(username)

                    if str(reaction.emoji) == "❌":
                        playerCounterComing = 1
                        playerCounterNotComing = 1
                        playerCounterLater = 1
                        username = str(user)
                        username = username.split("#")
                        username = username[0]
                        updateList = 1 
                        if any(username in s for s in playersListNotComing):
                            pass
                        else:
                            playersListNotComing.append(username)
                        if any(username in s for s in playersListComing):
                            playersListComing.remove(username)
                        if any(username in s for s in playersListLater):
                            playersListLater.remove(username)

                    if str(reaction.emoji) == "🕐":
                        playerCounterComing = 1
                        playerCounterNotComing = 1
                        playerCounterLater = 1
                        username = str(user)
                        username = username.split("#")
                        username = username[0]
                        updateList = 1   
                        if any(username in s for s in playersListComing):
                            playersListComing.remove(username)
                        if any(username in s for s in playersListNotComing):
                            playersListNotComing.remove(username)
                        if any(username in s for s in playersListLater):
                            pass
                        else:
                            playersListLater.append(username)


            except asyncio.TimeoutError:
                messageOutput += ("```prolog" + "\n" + "this " + gameName + " ready up check is already over.```")
                await botMessage.edit(messageOutput) 
                await channel.send("```prolog" + "\n" + gameName + " ready up check has now ended.```")
                break
        # print("Before try")
        # try:
        #     print("before message")
        #     message = await client.wait_for('message', timeout = 60* 10)
        #     print("after message")
        #     if str(message.content) == "move":
        #         for i in playersListComing:
        #             await client.move_member(i, 199476909275348995)
        # except asyncio.TimeoutError:
        #     print("ready move ended")
        oops = False
        
# @client.command(pass_context = True)
# async def move(ctx):
#     playersListComing = ["Cryogenics"]
#     for i in playersListComing:
#         await ctx.move_to(199476909275348995)
    
#remove reaction interaction 



        
# on_command = 0


            
        # for emoji in reactionEmojis:
        #     await ctx.message.add_reaction(emoji)
#=======================================



# #=======================================
#Covid cases
#========================================
@client.command(pass_context = True)
async def covid(ctx):
    print(str(ctx.message.author) +": $covid")
    result = casesinfo.mainCases()
    await ctx.send("```" + result[0] +"\n" + result[1] + "\n" + result[2] + "```")
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

# @client.command(pass_context = True)
# async def play(ctx, url):
#     try:
#         server = ctx.message.guild
#         voice_channel = server.voice_client
#         async with ctx.typing():
#             filename = await YTDLSource.from_url(url, loop=client.loop)
#             voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
#         await ctx.send('**Now playing:** {}'.format(filename))
#     except:
#             await ctx.send("The bot is not connected to a voice channel.")

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
#=====================
#Trial play
#=====================
@client.command()
async def play(ctx, url):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        em8 = discord.Embed(title = "Music Is Currently Playing", description = 'Please wait for the current playing music to end or use %leave <:_Paimon6:827074349450133524>.\nMusic provided by {ctx.author.mention} <:_Paimon6:827074349450133524>',color = ctx.author.color)
        await ctx.send(embed = em8)
        return

    voiceChannel = ctx.message.author.voice.channel
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    em6 = discord.Embed(title = "Downloading Youtube Music", description = f'{url}\n\nPlease wait for paimon to setup the music you provide.\nMusic provided by {ctx.author.mention} <:_Paimon6:827074349450133524>',color = ctx.author.color)
    await ctx.send(embed = em6, delete_after = 2)
    await ctx.message.delete()

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '196',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    em1 = discord.Embed(title = "Now Listening Youtube Music", description = f'{url}\n\nPlease use %leave first to change music.\nMusic provided by {ctx.message.author} <:_Paimon6:827074349450133524>',color = ctx.author.color)

    videoID = url.split("watch?v=")[1].split("&")[0]

    em1.set_thumbnail(url = f'https://img.youtube.com/vi/{videoID}/default.jpg'.format(videoID = videoID))
    await ctx.send(embed = em1)


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

