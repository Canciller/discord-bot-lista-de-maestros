import requests
import logging
from bs4 import BeautifulSoup
from fuzzywuzzy import fuzz

url_horarios = 'https://horarios.fime.me'
url_dependencia = f'{url_horarios}/dependencia/2316'
url_periodo = None

try:
    response = requests.get(url_dependencia)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')
        terms = soup.findAll('li', {'class': 'feature sombra-blanca'})
        if len(terms) > 0: url_periodo = f'{url_horarios}{terms[0].a["href"]}'
except Exception as e:
    logging.error(e)

def __scrap_materia(materia : str, url : str):
    try:
        response = requests.get(url)
        if not response:
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        materias = soup.findAll('li', { 'class': 'feature sombra-blanca' })

        match = []
        for el in materias:
            name = el.a.text.lower()

            name = name.replace('á', 'a')
            name = name.replace('é', 'e')
            name = name.replace('í', 'i')
            name = name.replace('ó', 'o')
            name = name.replace('ú', 'u')

            match.append(fuzz.ratio(name.lower(), materia))

        url_materia = f'{url_horarios}{materias[match.index(max(match))].a["href"]}'
        return url_materia

    except Exception as e:
        logging.error(e)

def __scrap(materia : str, url : str):
    try:
        response = requests.get(url)
        if not response:
            return None
        soup = BeautifulSoup(response.content, 'html.parser')
        letras = soup.findAll('a', { 'class': 'btn btn-default' })

        materia = materia.lower()
        url_materias = None
        for letra in letras:
            if materia.startswith(letra.text.lower()):
                url_materias = f'{url_horarios}{letra["href"]}'
                break

        return __scrap_materia(materia, url_materias)
    except Exception as e:
        logging.error(e)

def find(materia : str):
    return __scrap(materia, url_periodo)
