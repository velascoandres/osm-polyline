# OPEN STREET MAP - POLYLINE
Obtener polylines para armar rutas dadas las coordenadas:

## Instalacion

```shell script
    $ pip install -r requirements
```

## Uso
Tenemos dos ejemplos que hacen uso de los siguientes servicios web:
* [OSRM-API](http://project-osrm.org/) 
    ```shell script
      $ python openroute-service-ejemplo.py
    ```
    ```text
      Se debe solicitar una API-KEY
    ```
* [Open Route Service](https://openrouteservice.org/)
    ```shell script
      $ python osrm-api-ejemplo.py
    ```
  
## Resultados  
```json
{"coordinates": 
  [
    [-78.486192, -0.227976], 
    [-78.486194, -0.227974], 
    [-78.486454, -0.227849], 
    [-78.487097, -0.227407],
    [-78.484707, -0.246505], 
    [-78.484651, -0.246642], 
    [-78.484348, -0.247246], 
    [-78.484067, -0.247739],
    [-78.486192, -0.227976], 
    [-78.486194, -0.227974], 
    [-78.486454, -0.227849], 
    [-78.487097, -0.227407],
    [-78.484707, -0.246505], 
    [-78.484651, -0.246642], 
    [-78.484348, -0.247246], 
    [-78.484067, -0.247739]
  ], 
  "type": "LineString"
}
```
