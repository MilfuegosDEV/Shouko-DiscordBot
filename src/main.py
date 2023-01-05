import discord
from discord.ext import commands
from commands import jokes, ping

def token(path: str):
    """Requiere únicamente un parametro el cuál es la ruta donde se encuentra guardado el token, incluyendo la extensión de dicho archivo.\n\nRetorna el token."""
    with open(path, "r") as file:
        token = file.read()
    return token

intents = discord.Intents.all()

bot = commands.Bot("s!", intents=intents)


@bot.event
async def on_ready():
    activity = discord.activity.Game("s!help - más info")
    await bot.change_presence(activity=activity)
    print(f"{bot.user}> is logged on")


@bot.command(name="chiste")
async def __jokes(ctx):
    await jokes(ctx)


@bot.command(name="ping")
async def __ping(ctx):
    await ping(ctx, bot)


# Añadir token
bot.run(token=token(path=""))
