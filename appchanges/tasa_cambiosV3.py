import requests as consulta
from config import API_KEY
from model import *

modelo = ModelCoins()
modelo.getAllCoins(API_KEY)
###############################################################################

moneda = input("Ingrese un codigo de moneda: ").upper()

while not moneda.isalpha() or moneda not in modelo.valores_lista:
    moneda = input("Ingrese un codigo de moneda: ").upper()

modelo.updateExchange(API_KEY, moneda)