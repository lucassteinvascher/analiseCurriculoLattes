import Manipulacao as mp
import Dados as dd

# print(dd.bancoComissionados['Nome'])
dadosConvertidos = mp.conversaoCaracteres(dd.bancoComissionados['Nome'],' ','+')
URL = mp.CriarURLManipulacao(dadosConvertidos)
requisicao = mp.requisicaoNaWeb(URL)
novoBanco = mp.MatrizDeDados(dd.bancoComissionados['Nome'],URL,requisicao)
contador = 0
for i in novoBanco:
    print(novoBanco)




print('oi')