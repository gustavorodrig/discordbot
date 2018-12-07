import discord
from discord.ext import commands
from ctypes.util import find_library
import random
import logging
from discord import opus
from discord.ext.commands import Bot
import youtube_dl
import string



log = logging.getLogger(__name__)

if not discord.opus.is_loaded():
    opus_path = find_library("opus")
    discord.opus.load_opus(opus_path)

client = commands.Bot(command_prefix='#')

players = {}

contexto = None

async def play_youtube_url(link, ctx=contexto):
    print('Contexto %s', ctx)
    server = ctx.message.server
    print('Server %s', ctx)
    voice_bot = client.voice_client_in(server)
    player = await voice_bot.create_ytdl_player(link)
    players[server.id] = player
    player.start()


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

    global contexto
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)
    contexto = ctx

@client.command(pass_context=True)
async def play(ctx, link):
    await play_youtube_url(link, ctx)


@client.event
async def on_member_join(member):
    print("Recognized that " + member.name + " joined")
    await client.send_message(member, " BEM VINDO ")
    await client.send_message(discord.Object(id='CHANNELID'), 'Welcome!')
    print("Sent message to " + member.name)
    print("Sent message about " + member.name + " to #CHANNEL")

@client.event
async def on_message(message):

    lower_message = message.content.lower()

    if message.author == client.user:
        return
    if lower_message == "boa noite":
        play_youtube_url('https://www.youtube.com/watch?v=hPJVikuF1IIs')
        await client.send_message(message.channel, "Boa noite " + message.author.name + " se divirta muito!!!")

    await client.process_commands(message)

client.run("TOKEN")
