# Aplicación Python que permite almacenar información en InfluxDB

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
