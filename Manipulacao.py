import requests
from bs4 import BeautifulSoup
import Dados as dd


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
def requisicaoNaWeb(URL):
    resultados = []
    textoRetorno = ''
    tamanhoRetorno = 0
    for i in URL:
        r = requests.get(i)
        soup = BeautifulSoup(r.content, 'html.parser')
        textoRetorno = soup.find('div', class_='tit_form').get_text()
        resultados.append(textoRetorno)
        # resultados[1].append(textoRetorno.__len__())



    return resultados

def MatrizDeDados(nome,URL,textoRetorno):

    matriz = [[],[],[],[]]
    contador = 0

    for i in nome:

        matriz[0].append(nome[contador])
        matriz[1].append(URL[contador])
        matriz[2].append([contador])
        # matriz[3] = tamanhoTexto[contador]
        contador += 1

    return matriz


def TemOuNaoCurriculo(pessoa):

    for v in pessoa:

        contador = 0
        Auxiliar = ''

        for a in dd.alfabeto:
            if (v == a and contador < 9):
                Auxiliar += a
                contador += 1

    if (Auxiliar == 'Resultado'):
        print('teste1')
        return 1 # Tem curriculo

    else:
        print('teste2')
        return 0 #Não tem curriculo