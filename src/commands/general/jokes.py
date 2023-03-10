# jokes.py Changelogs
# Author: Juan Daniel Luna Cienfuegos
# GitHub: MilfuegosDEV
# version: 2.0.2

# v2.1.0
# Novedades:
# - Se ha recuperado el aportador del chiste y agregado al embed

# v2.0.1
# Cambios
# - El mensaje con el chiste paso de ser un simple mensaje de texto
#   a un mensaje de texto enriquecido "Embed"
# - El mensaje ya no se envia de una vez, ahora el bot responde al comando utilizado
#   con el chiste.


# v1.0.1
# Novedades:
# - Se añadio el comando s!chiste al bot


from bs4 import BeautifulSoup
import requests
import discord
from discord.ext import commands
from datetime import datetime


def __get_random_chiste():
    response = requests.get('http://www.chistes.com/ChisteAlAzar.asp?n=3')
    soup = BeautifulSoup(response.text, "html.parser")
    chiste = soup.find("div", "chiste").text

    colaboradorinfo = soup.find("div", "colaboradorinfo").text
    # información del que aporto el chiste
    info_owner = colaboradorinfo.split("-")
    info_owner = info_owner[0]  # Nombre del aportador

    return chiste, info_owner


def jokes(ctx: commands.Bot):
    """Muestra un chiste aleatorio en un mensaje de respuesta en un canal de Discord.
    
    Parameters:
    ctx (commands.Bot): Contexto del comando, que proporciona información sobre el mensaje que invocó el comando y el canal en el que se envió el mensaje.
    
    Returns:
    None: No devuelve ningún valor.
    """
    # Obtiene un chiste aleatorio y la información del autor
    __randomJoke = __get_random_chiste()
    # Crea una instancia de Embed
    embed = discord.Embed(description=__randomJoke[0])
    # Establece el autor del mensaje embed con el nombre del autor del chiste
    embed.set_author(name=__randomJoke[1])
    # Establece el pie de página del mensaje embed
    embed.set_footer(text="v2.1.0 • Hoy a las {}".format(
        datetime.today().strftime('%H:%M')))
    # Envía el mensaje embed de vuelta al canal de Discord
    return ctx.reply(embed=embed)
