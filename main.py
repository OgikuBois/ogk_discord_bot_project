import discord
import os 
import json 

riot_dev_api = "RGAPI-c84aa054-6d1f-4943-8604-a000551e68e2"


client = discord.Client()

bot_token = "ODc4NDkzNTkzODI2ODg1NjMy.YSB-6g.-sIJwqTiVdNHXMErM_TeVU5h2tI"

@client.event
async def on_ready():
    print('Logged on as {0}!'.format(client))

@client.event
async def on_message(message):
    print('Message from {0.author}: {0.content} in channel: {0.channel}'.format(message))


    if message.content.startswith("$hello"):
        await message.channel.send("You're a nice guy")

    # if message.content.startswith("$kc"):
    #     player_list = message.content.split(" ")
    #     kings_cup(player_list)



def kings_cup(player_list):
    pass




client.run(bot_token)

