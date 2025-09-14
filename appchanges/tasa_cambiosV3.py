import requests as consulta
from config import API_KEY
from model import *

modelo = ModelCoins()
modelo.getAllCoins(API_KEY)
###############################################################################

moneda = input("Ingrese un codigo de moneda: ").upper()

#or moneda not in modelo.valores_lista
while not moneda.isalpha():
    moneda = input("Ingrese un codigo de moneda: ").upper()

try:
    modelo.updateExchange(API_KEY, moneda)
    print("Rates: ", modelo.respuesta.get('quotes'))
    value1 = modelo.moneda+'EUR'
    value2 = modelo.moneda+'USD'
    print("EUR: ","{:.2F}€".format(modelo.respuesta['quotes'][value1]))
    print("USD: ","{:.2F}$".format(modelo.respuesta['quotes'][value2]))
except ModelError as error:
    print(error)