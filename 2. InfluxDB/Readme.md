# InfluxDB 3

## A. Comandos 

### 1. Descargamos e instalamos el software
    sudo curl -O https://www.influxdata.com/d/install_influxdb3.sh && sh install_influxdb3.sh
  
    source /home/admon/.bashrc
    influxdb3 --version
  
    mkdir  influxData
  
    cd influxData/


### 2. Levantamos el servicio
    influxdb3 serve --object-store=file --node-id=local01 --data-dir=/home/admon/influxData

### 3. Creamos un token de acceso (respaldamos el token)
    influxdb3 create token --admin --host http://localhost:8181

### 4. Declaramos una variable de ambiente que se asociará al token del punto anterior
    export INFLUXDB3_AUTH_TOKEN=apiv3_XXXXX

### 5. Creamos una base de datos llamada documentos
    influxdb3 create database documentos

### 6. Listamos las tablas
    influxdb3 query --database=documentos "SHOW TABLES"

## B. Video
Este video presenta instalación y configuación de InfluxDB 3.


