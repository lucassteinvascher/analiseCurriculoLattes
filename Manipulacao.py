###########  libraries ###########
import requests
from bs4 import BeautifulSoup
import Dados as dd

########## body ###########

def TemOuNaoCurriculo(pessoa):
    contador = 0
    Auxiliar = ''

    for v in pessoa:
        for a in dd.alfabeto:
            if (v == a and contador < 9):
                Auxiliar += a
                contador += 1

    if (Auxiliar == 'Resultado'):
        return 1 # Tem curriculo
    else:
        return 0 #Não tem curriculo


#dado um conjunto de dados, converte o valor procurado no esperado
def conversaoCaracteres(dados,procurado,esperado):
    NomesAuxiliares = []
    # dd.bancoComissionados['Nome']
    for n in dados:
        nomeAuxiliar = ''
        for l in n:
            if(l == procurado):
                nomeAuxiliar += str(esperado)
            else:
                nomeAuxiliar += l

        NomesAuxiliares.append(nomeAuxiliar)

    return NomesAuxiliares


# Dado conjunto de dados(lista com nomes previamente convertidos (' ' -> '+'),cria URL para manipulação
def CriarURLManipulacao(dados):
    URL = []
    for n in dados:
        URL.append('http://buscatextual.cnpq.br/buscatextual/busca.do?textoBusca='+str(n)+'&metodo=buscar')

    return URL


# Dada determinada URL(pagina web) Valida de itens passados na URL
def validaSeTemCurriculo(URL):

    for i in URL:
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html.parser')
        texto = soup.find('div', class_='tit_form').get_text()
        print(i)
        print(texto)
        print(texto.__len__())



