def ping(ctx, bot):
    return ctx.send(f"<@{ctx.author.id}> **Pong!** :ping_pong:\n:incoming_envelope: {round(bot.latency * 1000, 0)} ***ms***")