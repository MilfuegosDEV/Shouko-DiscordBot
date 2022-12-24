from bs4 import BeautifulSoup
import requests

def __get_random_chiste():
    response = requests.get('http://www.chistes.com/ChisteAlAzar.asp?n=3')
    soup = BeautifulSoup(response.text, "html.parser")
    chiste = soup.find("div", "chiste").text
    
    return chiste

def jokes(ctx):
    return ctx.send("<@{}> {}".format(ctx.author.id, __get_random_chiste()))