import requests
from bs4 import BeautifulSoup

i = ('http://buscatextual.cnpq.br/buscatextual/busca.do?textoBusca=steinvascher&metodo=buscar')

r = requests.get(i)
soup = BeautifulSoup(r.content, 'html.parser')
textoRetorno = soup.find('div', class_='resultado')

print(textoRetorno)

