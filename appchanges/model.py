import requests as consulta

class ModelError(Exception):
    pass

class ModelCoins():
    def __init__(self):
        self.url = ""
        self.lista_general = []
        self.valores_lista = []
        self.response = None
        self.moneda = None
        self.respuesta = [None]

    def getAllCoins(self, apikey):
        self.url = f"https://api.exchangerate.host/live?access_key={apikey}"
        self.response = consulta.get(self.url)

        if self.response.status_code != 200:
            raise Exception("Error en consulta de codigo:{}".format(self.response.status_code))
        
        self.lista_general = self.response.json()

        for k,v in self.lista_general['quotes'].items():
            self.valores_lista.append(k[3:])
        print("Lista: ",self.valores_lista)
        print("Total de monedas: ",len(self.valores_lista))

    def updateExchange(self, apikey, moneda):
        self.moneda = moneda
        r = consulta.get(f'https://api.exchangerate.host/live?access_key={apikey}&source={self.moneda}&currencies=EUR,USD')

        self.respuesta = r.json() #obtenemos la respuesta en formato de diccionario

        if r.status_code == 200:
            self.respuesta.get('quotes')
        else:
            raise ModelError(f"Error: {self.respuesta['error']['type']}: {self.respuesta['error']['info']}")
            