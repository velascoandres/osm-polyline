import requests
from utils import reversar, convertir_parametro_ruta

# Ejemplo con OSRM-API

coordenadas = [
    [-0.2279885, -78.4862021],
    [-0.2343332, -78.4841716],
    [-0.2373534, -78.4842575],
    [-0.2420552, -78.485494],
    [-0.2447133, -78.4849226],
    [-0.251262, -78.483007],
]
coordenadas_reversadas = list(map(reversar, coordenadas))
coordenadas_reversadas_str = list(map(convertir_parametro_ruta, coordenadas_reversadas))
separador = ';'
coordenadas_str = separador.join(coordenadas_reversadas_str)
url = f'http://router.project-osrm.org/route/v1/driving/{coordenadas_str}'
parametros = {
    'overview': 'full',
    'geometries': 'geojson'
}
respuesta_consulta = requests.get(url=url, params=parametros).json()
try:
    print(respuesta_consulta['routes'][0]['geometry'])
except IndexError:
    print(respuesta_consulta)
