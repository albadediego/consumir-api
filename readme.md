## Aplicación de consulta de valor actual de monedas y criptomonedas

Programa hecho en python para recuperar el valor en euros y dolares

# Instalación
- Obtener una apikey en https://exchangerate.host/
- Renombrar el fichero config_template.py a config.py
- Agregar dentro de config.py el apikey de esta manera:

```
API_KEY = 'aquí va tu apikey'
```

## Instalación de dependecias (librerías)
- Crear un entorno virtual de python con una de estas opciones:
```
py -m venv entorno
python -m venv entorno
python3 -m venv entorno
```
- Activar el entorno e instalar los requerimientos
```
windows: .\entorno\Scripts\activate
mac o linux: source entorno\bin\activate
```
```
pip install -r requirements.txt
```

-Utilizamos las librerías de pytest y request