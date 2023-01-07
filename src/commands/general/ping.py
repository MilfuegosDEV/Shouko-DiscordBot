import discord
from datetime import datetime
from discord.ext import commands


def ping(ctx, bot: commands.Bot):
    """Muestra la latencia del bot en un mensaje de respuesta en un canal de Discord.
    
    Parameters:
    ctx (commands.Context): Contexto del comando, que proporciona información sobre el mensaje que invocó el comando y el canal en el que se envió el mensaje.
    bot (commands.Bot): Instancia del bot que se está usando en Discord.
    
    Returns:
    None: No devuelve ningún valor.
    """
    # Crea una instancia de Embed
    embed = discord.Embed(
        description=f":ping_pong: **Pong!**\n:incoming_envelope: Mensajes: {int(round(bot.latency * 1000, 0))}ms")
    # Establece el pie de página del mensaje embed
    embed.set_footer(text="v2.0.1 • Hoy a las {}".format(
        datetime.today().strftime('%H:%M')))

    # Envía el mensaje embed de vuelta al canal de Discord
    return ctx.reply(embed=embed)