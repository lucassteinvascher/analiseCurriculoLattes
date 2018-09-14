import Manipulacao as mp
import Dados as dd

# print(dd.bancoComissionados['Nome'])
dadosConvertidos = mp.conversaoCaracteres(dd.bancoComissionados['Nome'],' ','+')
URL = mp.CriarURLManipulacao(dadosConvertidos)
requisicao = mp.requisicaoNaWeb(URL)
citados = mp.analisaCitacao(requisicao)
