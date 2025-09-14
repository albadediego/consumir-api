from appchanges.model import ModelCoins
from appchanges.config import API_KEY

def test_allcoins():
    objCoins = ModelCoins() #Creando objeto de la clase
    objCoins.getAllCoins(API_KEY) #Llamando al método getallcoins
    lista = objCoins.valores_lista
    assert lista != None #True
    cantidad = len(lista)
    assert cantidad == 171 #True

def test_exchange():
    cambio = ModelCoins()
    cambio.updateExchange(API_KEY, "BTC")
    assert len(cambio.respuesta) > 0
    assert cambio.respuesta != ""