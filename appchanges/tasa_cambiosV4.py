import requests as consulta
from config import API_KEY
from model import *
from view import *

modelo = ModelCoins()
modelo.getAllCoins(API_KEY)

vista = ViewCoins()
moneda = vista.insertCoin()

while not moneda.isalpha() or moneda not in modelo.valores_lista:
    moneda = vista.insertCoin()

try:
    modelo.updateExchange(API_KEY, moneda)
    vista.viewListCoins(modelo)
except ModelError as err:
    vista.getError(err)