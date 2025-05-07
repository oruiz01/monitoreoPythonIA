### Archivo:        InfluxDBWriter.py
### Versión:        1.0
### Autor:          Oscar Ruiz / oscarruiz@ciencias.unam.mx
### Fecha:          México, 7 de mayo 2025
### Observaciones:
###     Este código es una prueba de concepto.

### Hacemos el import de las bibliotecas
from influxdb_client_3 import Point, InfluxDBClient3
import os

### Creamos conexión a la base de datos
def getInfluxConnection():
    #print("Conexión a influxDB")
    tokenDB=os.environ.get("INFLUXDB3_AUTH_TOKEN")
    client = InfluxDBClient3(host='http://localhost:8181',database='documentos', token=tokenDB)
    #print("Connected!")
    ##print("------------------------------------------------")
    return client

def almacenaPointEnInfluxDB(clientInflux, nombreDeDocumento, tags, fields):
    #print(f"Nombre de documento: {nombreDeDocumento}")
    #print(f"Fields: {fields}")
    point = Point(nombreDeDocumento)

    for keyTag in tags.keys():
        #print(f"keyTag:{keyTag} value: {tags[keyTag]}")
        point=point.tag(keyTag,tags[keyTag])

    for key in fields.keys():
        #print(f"key:{key} value: {fields[key]}")
        point=point.field(key,fields[key])

    #print("Terminamos de armar point")
    #print("Almacenamos")
    clientInflux.write(point)
    #print("Stored")

def insert(tags, fields):
    clienteInflux= getInfluxConnection()
    print(f"Almacenamos datos en influxDB tags:{tags} \t fields:{fields}")
    almacenaPointEnInfluxDB(clienteInflux,"documentos",tags, fields)

