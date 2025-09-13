import requests as consulta
from config import API_KEY

moneda = input("Ingrese un codigo de moneda: ").upper()

while not moneda.isalpha():
    moneda = input("Ingrese un codigo de moneda: ").upper()

#todas las monedas
#https://api.exchangerate.host/live?access_key=TUAPIKEY
#https://api.exchangerate.host/live?access_key=TUAPIKEY&source=BTC&currencies=EUR,USD
    
#Invocando al metodo get con la url especifica
#https://api.exchangeratesapi.io/v1/latest?access_key=TUAPIKEY&base=EUR&symbols=USD,JPY

r = consulta.get(f'https://api.exchangerate.host/live?access_key={API_KEY}&source={moneda}&currencies=EUR,USD')
'''
print("codigo http de respuesta: ", r.status_code)
print("cabecera: ", r.headers['content-type'])
print("encoding: ", r.encoding)
print("respuesta en string: ", r.text)
print("respuesta en json: ", r.json())
'''

#Ejercicio 1: cómo capturamos el o los rates
respuesta = r.json() #obtenemos la respuesta en formato de diccionario
'''
print("Rates: ", respuesta.get('rates'))
print("USD: ", respuesta['rates']['USD'])
print("JPY: ", respuesta['rates']['JPY'])
'''

#Ejercicio 2: cómo capturo errores de peticion http
if r.status_code == 200:
    print("Rates: ", respuesta.get('quotes'))
    value1 = moneda+'EUR'
    value2 = moneda+'USD'
    print("EUR: ", round(respuesta['quotes'][value1], 2), "€")
    print("USD: ", round(respuesta['quotes'][value2], 2), "$")
else:
    print("Error: ", respuesta['error']['code']+": "+respuesta['error']['message'])