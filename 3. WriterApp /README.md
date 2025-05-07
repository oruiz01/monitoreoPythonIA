# Aplicación 1: Almacenamiento en InfluxDB con Python

### 1. Abrimos una terminal de comandos

### 2. Activamos el ambiente
    
    source /home/admon/venv/bin/activate
    
### 3. Instalamos el driver de InfluxDB para Python
    pip install influxdb3-python

### 4. Creamos un archivo con el nombre InfluxDBWriter.py

### 5. Anexamos el siguiente código
```python
### Archivo:        InfluxDBWriter.py
### Versión:        1.0
### Autor:          Oscar Ruiz / oscarruiz@ciencias.unam.mx
### Fecha:          México, 7 de mayo 2025
### Observaciones:
###     Este código es una prueba de concepto.

### Hacemos el import de las bibliotecas
from influxdb_client_3 import Point, InfluxDBClient3
import datetime
import os

### Obtenemos el token de acceso a la base de datos 
tokenDB=os.environ.get("INFLUXDB3_AUTH_TOKEN") 

### Creamos una conexion a InfluxDB
client = InfluxDBClient3(
host='http://localhost:8181',
database='documentos',
token=tokenDB
)

### Realizamos un write
print("WWWW:: Start write")
now= datetime.datetime.now()

### Formato de linea:
### Tabla       - Point()   :   cpu
### Tags:       - tag()     :   host=host01,region=us-west,application=webserver
### Valores:    - field()   :   val=1,usage_percent=20.5,status=OK
### Timestamp   now

#point="cpu,host=host01,region=us-west,application=webserver val=1,usage_percent=20.5,status=OK "+now
point = Point("cpu").tag("host", "host01").tag("region", "us-west").tag("application", "webserver").field("val", "1").field("usage_percent", 20.5).field("status", "OK")
print(point)
client.write(point)
print("WWWW:: End write")
```

### 6. Ejecutamos la aplicación
```bash
export INFLUXDB3_AUTH_TOKEN=apiv3_XXXXX
python InfluxDBWriter.py
WWWW:: Start write
cpu,application=webserver,host=host01,region=us-west status="OK",usage_percent=20.5,val="1"
WWWW:: End write
```


# Aplicación 2: Módulo de almacenamiento en InfluxDB con Python

### 1. Creamos un archivo con el nombre modulo_influxdb3.py

### 2. Anexamos el siguiente código
```python
### Archivo:        modulo_influxdb3.py
### Versión:        1.0
### Autor:          Oscar Ruiz / oscarruiz@ciencias.unam.mx
### Fecha:          México, 7 de mayo 2025

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
```

### 3. Creamos un archivo con el nombre InfluxDBWriter-v2.py

### 2. Anexamos el siguiente código
```python
### Archivo:        InfluxDBWriter-v2.py
### Versión:        1.0
### Autor:          Oscar Ruiz / oscarruiz@ciencias.unam.mx
### Fecha:          México, 7 de mayo 2025

### Hacemos el import de las bibliotecas
import modulo_influxdb3
import random
import time


# Variables
tags={}
tags["documentotag"]="-"
fields={}


#Declaramos un row a insertar
print("Inicializamos...")
fields["totaldocumentos"]=float(0)
fields["iddocumento"]=float(0)
fields["documento"]="-"
fields["totalpaginas"]=float(0)
fields["paginaactual"]=float(0)
fields["tiempo"]=float(0)
modulo_influxdb3.insert(tags,fields)
time.sleep(5)



## Procesamos documentos
totalDocumentos=10
pausa=5
print(f'Total documentos:{totalDocumentos}')

print("Procesamos documentos.... ")
for i in range(0, totalDocumentos):
    documentID=i+1
    totalPaginas=random.randint(1, 21)
    print(f'\ndocumentID:{documentID} - Total de paginas:{totalPaginas}')
    for pag in range(0, totalPaginas):
        paginaActual=pag+1
        tiempo=random.randint(1, 30)
        nombre=f'documento-{documentID}.pdf'
        print(f'documentID:{documentID} -  Nombre:{nombre} - Pagina:{paginaActual} - Tiempo:{tiempo}')
        time.sleep(5)
        #Almacenamos en grafana
        fields["totaldocumentos"]=float(totalDocumentos)
        fields["iddocumento"]=float(documentID)
        fields["documento"]=nombre
        fields["totalpaginas"]=float(totalPaginas)
        fields["paginaactual"]=float(paginaActual)
        fields["tiempo"]=float(tiempo)
        modulo_influxdb3.insert(tags,fields)

# Escribimos mensaje final
fields["iddocumento"]=float(0)
fields["documento"]="-"
fields["totalpaginas"]=float(0)
fields["paginaactual"]=float(0)
fields["tiempo"]=float(0)
modulo_influxdb3.insert(tags,fields)




#Fin
print("Terminamos.... ")

```


