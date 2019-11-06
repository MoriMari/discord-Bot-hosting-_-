import discord
import os
from discord import Game

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("테스트 중")
    await client.change_presence(status=discord.Status.online)


@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("나도 안녕!")
    if message.content.startswith("ㅎㅇㅎㅇ"):
        await message.channel.send("하이하이!")
    if message.content.startswith("능지처참누구?"):
        await message.channel.send("강꼰대!!")
    if message.content.startswith("우리돼지?"):
        await message.channel.send("한돈!")

        
access_token = os.environ["BOT_TOKEN"]       
client.run(access_token)
