import requests
from bs4 import BeautifulSoup

url_horarios = 'https://horarios.fime.me/dependencia/2316'

response = requests.get(url_horarios)
soup = BeautifulSoup(response.content, 'html.parser')

terms = soup.findAll('li', {'class': 'feature sombra-blanca'})
terms_links = []

for content in terms:
    link = content.a['href']
    term = content.text
    print(term + " ({})".format(link))