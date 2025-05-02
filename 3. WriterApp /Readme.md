# Aplicación Python que permite almacenar información en InfluxDB

### 1. Abrimos una terminal de comandos

### 2. Activamos el ambiente
    
    source /home/admon/venv/bin/activate
    
### 3. Instalamos el driver de InfluxDB para Python
    pip install influxdb3-python

### 4. Creamos aun archivo llamado InfluxDBWriter.py
    Anexamos el siguiente código

```python
### Hacemos el import de las bibliotecas
from influxdb_client_3 import Point, InfluxDBClient3
import datetime
import os

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
#point="cpu,host=host01,region=us-west,application=webserver val=1,usage_percent=20.5,status=OK "+now
point = Point("cpu").tag("host", "host01").tag("region", "us-west").tag("application", "webserver").field("val", "1").field("
usage_percent", 20.5).field("status", "OK")
client.write(point)

print("WWWW:: End write")


# Execute the query and return an Arrow table
table = client.query(
query="SELECT * FROM cpu LIMIT 10",
language="sql"
)
print("\n#### View Schema information\n")
print(table.schema)
print("\n#### Use PyArrow to read the specified columns\n")
print(table.column('application'))
print(table.column('usage_percent'))
print(table.select(['host', 'usage_percent']))
print(table.select(['time', 'host', 'usage_percent']))
print(table)
print("\n#### Use PyArrow compute functions to aggregate data\n")
```

### 5. Ejecutamos la aplicación
  
    python InfluxDBWriter.py

