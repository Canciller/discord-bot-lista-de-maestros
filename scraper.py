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

        rates = [
                find('chidos_score'),
                find('gachos_score')
                ]

        for score in scores:
            print(score.contents)

        for rate in rates:
            print(rate.span.contents)

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
            maestro = scrap(link.contents, link['href'])

            result.append(maestro)

        if len(result) == 0:
            return None
        return result
