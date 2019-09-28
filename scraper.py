import requests
from bs4 import BeautifulSoup

url = 'https://www.listademaestros.com/fime/buscar'

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
            result.append(link['href'])

        if len(result) == 0:
            return None
        return '\n'.join(result)
