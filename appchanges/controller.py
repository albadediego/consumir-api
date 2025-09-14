from appchanges.config import *
from appchanges.model import *
from appchanges.view import *

class controllerCoins():
    def executeProgram(self):
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