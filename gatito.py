import discord
import requests
from discord.ext import commands

# Define o token do bot do Discord (nunca compartilhe seu token real publicamente)
bot_token = 'Seu_Token'

# Configura as intenções do bot para receber mensagens de texto e conteúdo de mensagens
intents = discord.Intents.default()
intents.message_content = True

# Cria uma instância do bot com um prefixo para comandos (neste caso, '!')
client = commands.Bot(command_prefix='!', intents=intents)

# Evento que é acionado quando o bot está pronto e conectado
@client.event
async def on_ready():
    print("meow")  # Imprime "meow" no console quando o bot está pronto

# Comando para enviar uma imagem de gato
@client.command()
async def foto(ctx):
    # Faz uma requisição à API "The Cat API" para obter uma imagem de gato
    image_url = requests.get('https://api.thecatapi.com/v1/images/search').json()[0]['url']
    await ctx.send(image_url)  # Envia o URL da imagem para o canal

# Comando para enviar um GIF ou vídeo de gato
@client.command()
async def gif(ctx):
    # Faz uma requisição à API "The Cat API" para obter um GIF ou vídeo de gato
    video_url = requests.get('https://api.thecatapi.com/v1/images/search?mime_types=gif,mp4').json()[0]['url']
    await ctx.send(video_url)  # Envia o URL do vídeo para o canal

# Comando para enviar um arquivo de áudio de um gato miando
@client.command()
async def miau(ctx):
    # Nome do arquivo de áudio
    audio_file = 'miau.mp3'
    # Envia o arquivo de áudio para o canal
    await ctx.send(file=discord.File(audio_file))

# Comando para exibir uma lista de comandos disponíveis
@client.command()
async def ajuda(ctx):
     await ctx.send("!foto \n!gif\n!miau")  # Envia uma mensagem listando os comandos disponíveis

# Inicia o bot usando o token
client.run(bot_token)
