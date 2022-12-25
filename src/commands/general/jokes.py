from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands
from datetime import datetime


def __get_random_chiste():
    response = requests.get('http://www.chistes.com/ChisteAlAzar.asp?n=3')
    soup = BeautifulSoup(response.text, "html.parser")
    chiste = soup.find("div", "chiste").text

    return chiste


def jokes(ctx: commands.Bot):
    # embed
    embed = discord.Embed(description=__get_random_chiste())

    # footer
    embed.set_footer(text="v2.0.1 • Hoy a las {}".format(
        datetime.today().strftime('%H:%M')))

    return ctx.reply(embed=embed)
