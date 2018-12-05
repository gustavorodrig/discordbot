import discord
from discord.ext import commands
from discord.ext.commands import Bot
import random
import youtube_dl
import string

# client = discord.Client()
client = commands.Bot(command_prefix='#')

players = {}

@client.event
async def on_ready():
    print('Cheguei caralho!!')
    print(client.user.name)
    print(client.user.id)
    print('------')
    await client.change_presence(game=discord.Game(name="Bot dos Feeders"))

@client.command(pass_context=True)
async def perolas(ctx):
    print("teste")
    perolas = ["Só voltou o que deu! - Alemaosin",
               "Acordei hoje com uma puta dor de garganta arrombada - Barata",
               "Dragão da Noite - Fer",
               "Natural pra cavalo - Insanno"]

    await client.say(random.choice(perolas))

@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)

@client.command(pass_context=True)
async def play(ctx,  url):

    server = ctx.message.server
    voice_bot = client.voice_client_in(server)
    player = await voice_bot.create_ytdl_player(url)
    players[server.id] = player
    player.start()

@client.event
async def on_message(message):

    message.content = message.content.lower()

    if message.author == client.user:
        return
    if message.content == "boa noite":
        await client.send_message(message.channel, "Boa noite " + message.author.name + " se divirta muito!!!")

    await client.process_commands(message)

client.run("NTE4ODgyMTYxMDY4MjEyMjI2.DuXOlg.tihQu0yAZrYS_L034u3R5H03EQg")
