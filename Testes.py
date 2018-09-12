###########   libraries ###########

import requests
from bs4 import BeautifulSoup
import pandas as pd

###########   header    ###########
Auxiliar = ''
NomesAuxiliares = []
nomeAuxiliar = ''
contador = 0
URL = []
alfabeto = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
            'V', 'W', 'X', 'Y', 'Z']

banco = pd.read_csv('Comissionados.csv')

r = requests.get(
    'http://buscatextual.cnpq.br/buscatextual/busca.do?textoBusca=Lucas+de+Moura+Steinvascher&metodo=buscar')

##########   body       ###########

soup = BeautifulSoup(r.content, 'html.parser')
texto = soup.find('div', class_='tit_form').get_text()
vetor = [texto]

# Manipula a URL e retorna se tem ou não curriculo
def TemOuNaoCurriculo():
    contador = 0
    Auxiliar = ''

    for v in vetor[0]:
        for a in alfabeto:
            if (v == a and contador < 9):
                Auxiliar += a
                contador += 1

    if (Auxiliar == 'Resultado'):
        return 1 # Tem curriculo
    else:
        return 0 #Não tem curriculo



# manipula o arquivo csv e converte o nome para informar na URL
for n in banco['Nome']:
    nomeAuxiliar = ''
    for l in n:
        if (l == ' '):
            nomeAuxiliar += '+'
        else:
            nomeAuxiliar += l

    NomesAuxiliares.append(nomeAuxiliar)

# Criando URL Para manipulação
for n in NomesAuxiliares:
    URL.append('http://buscatextual.cnpq.br/buscatextual/busca.do?textoBusca=' + str(n) + '&metodo=buscar')
    print(n)


