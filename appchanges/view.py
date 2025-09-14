from datetime import datetime

class ViewCoins:
    def insertCoin(self):
        moneda = input("Ingrese un codigo de moneda: ").upper()
        return moneda
    
    def viewListCoins(self, modelo):
        print("Rates: ", modelo.respuesta.get('quotes'))
        value1 = modelo.moneda+'EUR'
        value2 = modelo.moneda+'USD'
        datos = f"EUR: { '{:.2f}€'.format(modelo.respuesta['quotes'][value1]) }\nUSD: { '{:.2f}$'.format(modelo.respuesta['quotes'][value2]) }\nFecha: { datetime.fromtimestamp(modelo.respuesta.get('timestamp')) }\nMoneda: { modelo.respuesta.get('source') }"
        print(datos)

    def getError(self, error):
        print(error)