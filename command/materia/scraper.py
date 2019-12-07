import requests
import logging
from bs4 import BeautifulSoup
import imgkit
from PIL import Image
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

def __crop(image, coords, saved_location):
    cropped_image = image.crop(coords)
    cropped_image.save(saved_location)

def __scrap_materia(materia : str, url : str):
    try:
        """
        response = requests.get(url)
        if not response:
            return None

        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.table
        if not table:
            return None

        horarios = []
        for r in table.findAll('tr'):
            h = []
            for c in r.findAll('td'):
                if len(c.text) > 0:
                    h.append(c.text)
            if len(h) > 0:
                horarios.append(h)
        """

        img = imgkit.from_url(url, 'out.png')
        img = Image.open('out.png')
        width, height = img.size

        img = __crop(img, (0, 640, width, height-207), 'out-cropped.png')

        return {
                'name': materia,
                'url': url
                }

    except Exception as e:
        logging.error(e)

def __scrap_materias(materia : str, url : str):
    try:
        response = requests.get(url)
        if not response:
            return None

        soup = BeautifulSoup(response.content, 'html.parser')
        materias = soup.findAll('li', { 'class': 'feature sombra-blanca' })

        materia = materia.replace('1', 'I')
        materia = materia.replace('2', 'II')
        materia = materia.replace('3', 'III')
        materia = materia.replace('4', 'IV')
        materia = materia.replace('5', 'V')

        match = []
        for el in materias:
            name = el.a.text.lower()

            name = name.replace('á', 'a')
            name = name.replace('é', 'e')
            name = name.replace('í', 'i')
            name = name.replace('ó', 'o')
            name = name.replace('ú', 'u')

            match.append(fuzz.ratio(name.lower(), materia.lower()))

        maxIndex = match.index(max(match))
        materia = materias[maxIndex].text

        url_materia = f'{url_horarios}{materias[maxIndex].a["href"]}'
        return __scrap_materia(materia, url_materia)

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

        return __scrap_materias(materia, url_materias)
    except Exception as e:
        logging.error(e)

def find(materia : str):
    return __scrap(materia, url_periodo)
