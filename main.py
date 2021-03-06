import os
import discord
import youtube_dl
from discord.ext import commands
import json
import requests

#Prajnadeep Das
#20-06-2021
client = commands.Bot(command_prefix="&")


@client.command()
async def play(ctx, url: str):
    song_there = os.path.isfile("song.mp3")
    try:
        if song_there:
            os.remove("song.mp3")
    except PermissionError:
        await ctx.send("Wait for the current playing music to end or use the 'stop' command")
        return

    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name='General')
    await voiceChannel.connect()
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    for file in os.listdir("./"):
        if file.endswith(".mp3"):
            os.rename(file, "song.mp3")
    voice.play(discord.FFmpegPCMAudio("song.mp3"))
    await ctx.channel.send("Playing music.")
    print("Log:: Playing music.")


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")


@client.command()
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently no audio is playing.")


@client.command()
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("The audio is not paused.")


@client.command()
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    voice.stop()

@client.command()
async def joke(ctx):
    data = requests.get("https://official-joke-api.appspot.com/random_joke")
    y = json.loads(data.text)
    await ctx.channel.send(y["setup"])  # Prints the joke question
    await ctx.channel.send(y["punchline"])  # Prints the joke answer


@client.command()
async def hello(ctx):
    await ctx.channel.send("Hello, I am a test bot [@DareDevil Bot].")
    await ctx.channel.send("Currently under development.")
    await ctx.channel.send("Author :: ??????????#5258")
    await ctx.channel.send("Prefix: &")
    await ctx.channel.send("Current commands: play youtube_url,joke")

client.run('YOUR TOKEN HERE')
