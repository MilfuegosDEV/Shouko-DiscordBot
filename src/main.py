import discord
from discord.ext import commands
from commands import jokes,ping

intents = discord.Intents.all()

bot = commands.Bot("s!", intents= intents)

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
    message = ctx.message
    await message.delete()
    await ping(ctx, bot)


bot.run(token="") # Añadir tokend