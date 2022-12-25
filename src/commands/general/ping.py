import discord
from datetime import datetime
from discord.ext import commands


def ping(ctx, bot: commands.Bot):
    # embed
    embed = discord.Embed(
        description=f":ping_pong: **Pong!**\n:incoming_envelope: Mensajes: {int(round(bot.latency * 1000, 0))}ms")
    # footer
    embed.set_footer(text="v2.0.1 • Hoy a las {}".format(
        datetime.today().strftime('%H:%M')))

    return ctx.reply(embed=embed)
