import discord
from discord.ext import commands,tasks
import os 
import json 
import youtube_dl


riot_dev_api = "RGAPI-c84aa054-6d1f-4943-8604-a000551e68e2"


client = discord.Client()

fd = open("bot_token.txt", "r")
bot_token = fd.read()

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client))

@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content} in channel: {0.channel}'.format(message))
    message.content = message.content.lower()

    if message.content.startswith("$hello"):
        await message.channel.send("Hello {}".format(message.author))

    if message.content.startswith("$help") or message.content.startswith("$commands"):
        await message.channel.send("$hello || Displays a hello message.\n$play `{YouTube link or video name`}\n")

    if message.content.startswith("$play"):
        song = ""
        messageContent = message.content.strip().split(" ")
        for i in range(1, len(messageContent)):
            song += messageContent[i] + " "
        await message.channel.send("!play" + " " + song)

    if message.content.startswith("$join"):
        # channel = message.author.voice.channel
        # await message.channel.send(channel.id)
        # await channel.connect()
        connected = message.author.voice
        if connected:
            await connected.channel.connect()

    # if message.content.startswith("~kc"):
    #     player_list = message.content.split(" ")
    #     kings_cup(player_list)



def kings_cup(player_list):
    pass


client.run(bot_token)

