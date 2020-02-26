import requests
from openrouteservice import convert
from utils import reversar


# Ejemplo con open-route-service

# api-endpoint
URL = 'https://api.openrouteservice.org/v2/directions/driving-car'
API_KEY = '5b3ce3597851110001cf62483ad9c77a1cc94f13a94ea2f28f226411'

# En este caso tengo coordenadas en este orden: [lat, lon]
coordenadas = [
    [-0.2279885, -78.4862021],
    [-0.2343332, -78.4841716],
    [-0.2373534, -78.4842575],
    [-0.2420552, -78.485494],
    [-0.2447133, -78.4849226],
    [-0.251262, -78.483007],
]
# Las coordenadas deben estar en este orden -> [lon, lat]
coordenadasReversadas = list(map(reversar, coordenadas))

datos = {
    'coordinates': coordenadasReversadas,
}

cabeceras = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
    'Authorization': API_KEY,
    'Content-Type': 'application/json; charset=utf-8'
}
r = requests.post(url=URL, headers=cabeceras, json=datos)

data = r.json()
# Las cooredadas del polyline estan codificadas
geometria_codificada = data['routes'][0]['geometry']
geometria_descodificada = convert.decode_polyline(geometria_codificada)
# Coordenadas para dibujar las lineas
# {'type': 'LineString', 'coordinates': [[-78.48619, -0.22798], [-78.48619, -0.22797] ..]}
print(geometria_descodificada)
