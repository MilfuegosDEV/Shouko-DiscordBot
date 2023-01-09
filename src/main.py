import discord
from discord.ext import commands
from commands import jokes, ping
from games import typing


def token(path: str) -> str:
    """
    Lee el token del bot de un archivo de texto y lo devuelve.

    Parameters:
    path (str): La ruta del archivo que contiene el token, incluyendo la extensión del archivo.

    Returns:
    str: El token del bot.
    """
    with open(path, "r") as file:
        token = file.read()
    return token


intents = discord.Intents.all()

bot = commands.Bot("s!", intents=intents)


@bot.event
async def on_ready():
    """Muestra un mensaje cuando el bot se conecta al servidor y cambia la actividad del perfil del bot."""
    activity = discord.activity.Game("s!help - más info")
    await bot.change_presence(activity=activity)
    print(f"{bot.user}> is logged on")


@bot.command(name="chiste")
async def __jokes(ctx):
    """Muestra un chiste aleatorio en el canal de Discord."""
    await jokes(ctx)


@bot.command(name="ping")
async def __ping(ctx):
    """Muestra la latencia del bot en el canal de Discord."""
    await ping(ctx, bot)


@bot.command(name="type")
async def __type(ctx):
    """Realiza un test de escritura en el canal de Discord y muestra los resultados."""
    await typing(ctx, bot)

# Conecta el bot al servidor de Discord
bot.run(token=token(path="token.txt"))