import random
import discord
import asyncio
from discord.ext import commands
from datetime import datetime
import time


def __GiveMeSomeRandomWords() -> list:
    wordList = ['lo', 'bien', 'mañana', 'siempre', 'gracias', 'casa', 'estaba', 'todos', 'pasa', 'al', 'él', 'con', 'poco', 'ese', 'has', 'ti', 'nuevo', 'nadie', 'tiempo', 'sabes', 'haciendo', 'sabes', 'desde', 'uno', 'tú', 'quiere', 'dos', 'quien', 'dije', 'sin', 'he', 'acuerdo', 'mundo', 'ir', 'mía', 'como', 'tengo', 'en', 'años', 'y', 'ver', 'hace', 'hasta', 'cosas', 'les', 'quieres', 'también', 'cosas', 'qué', 'gran', 'espero', 'para', 'fue', 'te', 'que', 'lugar', 'puedes', 'este', 'después', 'ya', 'pasa', 'ha', 'no', 'este', 'dónde', 'el', 'estas', 'sí', 'vamos', 'momento', 'podría', 'algo', 'oh', 'ahora', 'le', 'tu', 'eres', 'lugar', 'ni', 'el', 'amigo', 'podría', 'buena', 'vamos', 'si', 'dos', 'los', 'aquí', 'más', 'sabe', 'mejor', 'has', 'vez', 'hija', 'claro', 'la', 'estado', 'soy', 'espero', 'quiero', 'se', 'por', 'vas', 'era', 'mis', 'a', 'después', 'hola', 'antes', 'otro', 'siento', 'ese', 'ahí', 'ahora', 'ni', 'al', 'los', 'años', 'todo', 'es', 'me', 'quieres', 'las', 'noche', 'casa', 'usted', 'estas', 'tan', 'esa', 'tiene', 'todo', 'hola', 'dios', 'al', 'solo', 'estaba', 'podemos', 'muy', 'todos', 'dinero', 'solo', 'dinero', 'todo', 'otra', 'ella', 'bueno', 'vida', 'día', 'ver', 'dios', 'tal', 'mucho', 'favor', 'tiene', 'nunca', 'sabe', 'los', 'también', 'ti', 'crees', 'voy', 'gusta', 'papas', 'verdad', 'mi', 'me', 'como', 'no', 'hay', 'tú', 'tengo', 'espero', 'lo', 'en', 'necesito', 'padre', 'una', 'por', 'usted', 'necesito', 'de', 'alguien', 'soy', 'tener', 'dije', 'fue', 'sé', 'vas', 'esta', 'creo', 'porque', 'quien', 'eres', 'quiere', 'mí', 'parece', 'o',
                'parece', 'que', 'tipo', 'será', 'mismo', 'esto', 'trabajo', 'nombre', 'estoy', 'las', 'puedes', 'puedo', 'soy', 'tu', 'gente', 'tipo', 'eso', 'buena', 'sin', 'mi', 'nuestro', 'o', 'trabajo', 'estamos', 'lo', 'estás', 'necesito', 'verdad', 'ella', 'han', 'nuevo', 'mucho', 'tenemos', 'has', 'ir', 'ti', 'tener', 'vez', 'nos', 'sus', 'un', 'señor', 'ni', 'hacer', 'su', 'el', 'será', 'hombre', 'porque', 'solo', 'su', 'yo', 'eres', 'sí', 'mía', 'a', 'ser', 'a', 'crees', 'muy', 'esta', 'señor', 'podemos', 'sus', 'ella', 'tienes', 'puede', 'parece', 'como', 'eso', 'él', 'solo', 'gran', 'entonces', 'vas', 'dije', 'sobre', 'seguro', 'noche', 'si', 'crees', 'ahí', 'dice', 'nuestro', 'ahí', 'la', 'he', 'qué', 'hace', 'la', 'algo', 'como', 'nuestro', 'un', 'puede', 'nos', 'acuerdo', 'o', 'hablar', 'hablar', 'yo', 'creo', 'del', 'ser', 'ellos', 'nunca', 'entonces', 'mira', 'es', 'días', 'haciendo', 'estoy', 'hola', 'día', 'día', 'te', 'amigo', 'así', 'quiere', 'sabes', 'podemos', 'antes', 'nunca', 'siempre', 'ellos', 'su', 'se', 'les', 'nuevo', 'solo', 'cuando', 'decir', 'nosotros', 'qué', 'vida', 'antes', 'dios', 'dónde', 'cosa', 'dije', 'hacer', 'será', 'gracias', 'tú', 'otro', 'sobre', 'solo', 'voy', 'alguien', 'poco', 'usted', 'mira', 'ese', 'seguro', 'va', 'tiempo', 'más', 'cosas', 'mí', 'tipo', 'cosa', 'este', 'seguro', 'sea', 'tienes', 'eso', 'mí', 'estoy', 'noche', 'puedes', 'yo', 'del', 'hablar', 'siento', 'desde', 'era', 'que', 'buena', 'tus', 'tu', 'mismo', 'mía', 'bien', 'ahora', 'hija', 'estaba', 'son', 'una', 'vez', 'tiene', 'hay', 'dije', 'pero', 'nada', 'alguien']

    __generatedList: list = []
    for i in range(35+1):
        __generatedList.append(random.choice(wordList))
    return __generatedList


def __listToSTR(__generatedList: list) -> str:
    text = ""
    for i in __generatedList:
        text += i + " "
    return text.strip()

def calc_typing_accuracy(original_list: list, test_list: list) -> float:
    """
    Calcula la precisión de la mecanografía comparando dos listas de palabras.
    
    Parameters:
    original_list (list): La lista de palabras aleatorias generadas por la computadora.
    test_list (list): La lista de palabras escritas por el usuario.
    
    Returns:
    float: El porcentaje de precisión de la mecanografía (entre 0 y 100).
    """
    mistaked: int = 0
    for i in range(35):  # Iterar a través de las primeras 35 palabras
        try:
            # Incrementar el contador de errores si la palabra no coincide
            if test_list[i] != original_list[i]:
                mistaked += 1
        except IndexError:
            # Si una lista es más corta que la otra, se considera un error
            mistaked += 1

    # Calcular el porcentaje de errores
    wrong_percent = (mistaked / len(original_list) * 100)

    # Devolver el porcentaje de aciertos
    return (100 - wrong_percent)


async def typing(ctx: commands.Bot, bot: commands.Bot):
    """
    Realiza un test de escritura en el canal de Discord donde se ejecutó el comando.
    
    Parameters:
        ctx (commands.Bot): El contexto del comando.
        bot (commands.Bot): El bot de Discord.
    
    Returns:
        None
    """
    
    # Muestra un mensaje de cuenta regresiva antes de comenzar el test de escritura
    for sec in range(3, 0, -1):
        await asyncio.sleep(1)
        if sec == 3:
            message = await ctx.reply(f"Escribe el siguiente texto en negrita para medir tu velocidad:\nEmpezando en {sec} segundos!")
        elif sec == 2:
            await message.edit(content=f"Escribe el siguiente texto en negrita para medir tu velocidad:\nEmpezando en {sec} segundos!")
        else:
            await message.edit(content=f"Escribe el siguiente texto en negrita para medir tu velocidad:\nYAAAAAAAA!!!!!")
    
    # Obtiene una lista de palabras aleatorias y la convierte en una cadena de texto en negrita
    original_list = __GiveMeSomeRandomWords()
    text = __listToSTR(original_list)
    
    await message.edit(content=f"Escribe el siguiente texto en negrita para medir tu velocidad:**\n{text}**")
    
    # Toma el tiempo actual
    time1 = time.time()
    
    # Define una función de comprobación para validar si el mensaje proviene del autor del comando
    def checkingTest(reply):
        return ctx.author == reply.author
    
    # Bloquea el hilo hasta que se recibe un mensaje que pase la comprobación de checkingTest
    try:
        msg = await bot.wait_for("message", check=checkingTest, timeout=60.0)
    except asyncio.TimeoutError:
        # Si el usuario no responde al mensaje dentro de 60 segundos, se enviará un mensaje indicando que no se ha finalizado la prueba.
        
        await message.delete() # se elimina la prueba
        
        # Se envia un Embed indicando el estado.
        embed=discord.Embed(title="Se ha acabado el tiempo", color=0x9d0101)
        embed.add_field(name="Velocidad", value=f"No aplica", inline=True)
        embed.add_field(name="Precisión", value=f"No aplica", inline=True)
        embed.add_field(name="Tiempo tomado", value=f"No aplica", inline=True)
        embed.set_footer(text="v1.0.1 • Hoy a las {}".format(
            datetime.today().strftime('%H:%M')))
        await ctx.reply(embed=embed)
        
    else:
        # Toma el tiempo actual de nuevo
        time2 = time.time()
        
        # Calcula el tiempo transcurrido, la velocidad de escritura en wpm y la precisión
        total_time = int(time2 - time1)
        wpm = len(msg.content) * 60 / (5 * total_time)
        accuracy = calc_typing_accuracy(original_list, msg.content.split())
        
        # Elimina el los mensajes de la prueba.
        await message.delete() # Mensaje generado por el bot
        await msg.delete() # Mensaje generado por el usuario
        
        # Responde con un embed al canal con la velocidad de escritura, la precisión del usuario y el tiempo tomado
        embed=discord.Embed(title="Resultados", color=0x0b9d01)
        embed.add_field(name="Velocidad", value=f"{wpm:.0f} WPM", inline=True)
        embed.add_field(name="Precisión", value=f"{accuracy:.0f}%", inline=True)
        embed.add_field(name="Tiempo tomado", value=f"{total_time} segundos", inline=True)
        embed.set_footer(text="v1.0.1 • Hoy a las {}".format(
            datetime.today().strftime('%H:%M')))
        await ctx.reply(embed=embed)
