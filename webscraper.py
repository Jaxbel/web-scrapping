import re
from colorama import Fore
import requests

website="https://es.wikipedia.org/wiki/Hermes_Trismegisto"
resultado= requests.get(website)
content = resultado.text


patron = r"mw-[\w-]*"
titulos= re.findall(patron,content)
sinduplicados= list (set(titulos))

titulos_final=[]

for i in sinduplicados:
    titulo_de_titulo = i.replace("mw-","")
    titulos_final.append(titulo_de_titulo)
    print(titulo_de_titulo)



