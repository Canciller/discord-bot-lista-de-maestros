import requests
from bs4 import BeautifulSoup

url = 'https://www.listademaestros.com/fime/buscar'

def scrap(name, url):
    response = requests.get(url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')

        def find(id):
            return soup.find(id = id)

        scores = [
                find('ex_li'),
                find('ac_li'),
                find('pa_li'),
                find('as_li'),
                find('se_li')
                ]

        chidos = find('chidos_score')
        gachos = find('gachos_score')

        maestro = {
                'name' : name,
                'url' : url
                }

        for score in scores:
            value = float(score.contents[0])
            key = score.contents[1].text
            maestro[key] = value;

        maestro['Chidos'] = int(chidos.span.text)
        maestro['Gachos'] = int(gachos.span.text)

        return maestro

def find(name : str):
    if not name:
        return None

    result = []
    target_url = f'{url}/{name}'

    response = requests.get(target_url)
    if response:
        soup = BeautifulSoup(response.content, 'html.parser')

        table = soup.find(id = 'nombres_table')
        for link in table.find_all('a'):
            maestro = scrap(link.text, link['href'])

            result.append(maestro)

        if len(result) == 0:
            return None
        return result
