class ViewCoins:
    def insertCoin(self):
        moneda = input("Ingrese un codigo de moneda: ").upper()
        return moneda
    
    def viewListCoins(self, modelo):
        print("Rates: ", modelo.respuesta.get('quotes'))
        value1 = modelo.moneda+'EUR'
        value2 = modelo.moneda+'USD'
        print("EUR: ","{:.2F}€".format(modelo.respuesta['quotes'][value1]))
        print("USD: ","{:.2F}$".format(modelo.respuesta['quotes'][value2]))

    def getError(self, error):
        print(error)