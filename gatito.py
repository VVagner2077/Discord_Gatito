import discord
import requests
from discord.ext import commands



bot_token = 'Seu_token'

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix='!', intents=intents)

@client.event
async def on_ready():
    print("meow")

@client.command()
async def foto(ctx):
    image_url = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
    await ctx.send(image_url)

@client.command()
async def gif(ctx):
    video_url = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif,mp4').json()[0]['url']
    await ctx.send(video_url)

@client.command()
async def miau(ctx):
  
    audio_file = 'miau.mp3'

    await ctx.send(file=discord.File(audio_file))

client.run(bot_token)
    