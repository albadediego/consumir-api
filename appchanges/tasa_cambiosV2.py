import requests as consulta
from config import API_KEY

#Consulto todas las monedas
#https://api.exchangerate.host/live?access_key=TUAPIKEY
url = f"https://api.exchangerate.host/live?access_key={API_KEY}"
response = consulta.get(url)

if response.status_code != 200:
    raise Exception("Error en consulta de codigo:{}".format(response.status_code))

lista_general = response.json()

valores_lista=[]
for k,v in lista_general['quotes'].items():
    valores_lista.append(k[3:])

print("Lista: ",valores_lista)
print("Total de monedas: ",len(valores_lista))
###############################################################################

moneda = input("Ingrese un codigo de moneda: ").upper()

while not moneda.isalpha() or moneda not in valores_lista:
    moneda = input("Ingrese un codigo de moneda: ").upper()

r = consulta.get(f'https://api.exchangerate.host/live?access_key={API_KEY}&source={moneda}&currencies=EUR,USD')

respuesta = r.json() #obtenemos la respuesta en formato de diccionario

if r.status_code == 200:
    print("Rates: ", respuesta.get('quotes'))
    value1 = moneda+'EUR'
    value2 = moneda+'USD'
    print("EUR: ", round(respuesta['quotes'][value1], 2), "€")
    print("USD: ", round(respuesta['quotes'][value2], 2), "$")
else:
    print("Error: ", respuesta['error']['code']+": "+respuesta['error']['message'])