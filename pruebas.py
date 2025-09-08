respuesta =  {'success': True, 'timestamp': 1757355544, 'base': 'EUR', 'date': '2025-09-08', 'rates': {'USD': 1.175047, 'JPY': 173.442807}}

print(respuesta['rates'])
print(respuesta.get('rates'))
rates = respuesta.get('rates')
print('USD: ', rates.get('USD'))
print('JPY: ', rates.get('JPY'))