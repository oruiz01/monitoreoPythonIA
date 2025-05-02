# Configuración de Grafana

### 1. Ingresamos a https://grafana.org
    Seleccionamos * Open Source / Grafana *

![image](https://github.com/user-attachments/assets/d52a4a6b-a744-4820-ba51-3ef24c0effee)

### 2. Seleccionamos Download

### 3.	Seleccionamos Linux
![image](https://github.com/user-attachments/assets/3865ac5f-3873-44c9-ab7e-8a0d4b7428ca)

### 4. Instalamos una utilería requerida por Grafana
    sudo apt-get install -y adduser libfontconfig1 musl

### 5. Instalamos Grafana
    sudo dpkg -i grafana-enterprise_11.6.1_amd64.deb

### 6. Hacemos un refresh de los servicios de Ubuntu
    systemctl daemon-reload

### 7. Levantamos el servicio de Grafana
    sudo /bin/systemctl start grafana-server

### 8. Abrimos un navegador y accedemos a http://localhost:3000  

### 9. Ingresamos con la contraseña:  admin / admin
      Nos pedirá asignar un nuevo password.

### 10. Nos presenta la siguiente pantalla
![image](https://github.com/user-attachments/assets/a7ec93a9-83a4-45dd-a8bf-09a94bdd7a32)

### 11. Registramos el recurso InfluxDB en Grafana

    Seleccionamos Grafana / Connections / Data sources / Add data source
![image](https://github.com/user-attachments/assets/01a117ed-8856-4be6-b561-bb9f0702b8e4)

    Seleccionamos InfluxDB
![image](https://github.com/user-attachments/assets/850205b2-51b6-4a5f-b21a-c4a6e0926cab)

    Definimos los siguientes valores:
    Name:              influxdb-sql
    Query Language:    SQL 
    URL:               http://localhost:8181
    Database:          documentos
    Token:             apiv3_XXXXXX (Este valor se obtuvo en el módulo 2. InfluxDB)
    Insescure Connection: Habilitado

![image](https://github.com/user-attachments/assets/22e68b30-6dab-4c22-9475-3c6da886fab3)
    
    Al final de la página seleccionamos Save & test
![image](https://github.com/user-attachments/assets/2ce72374-6d99-4c59-8525-ee7bb0493a23)

    Si marca error de conexión:
    - Crea un nuevo Token (Ver módulo 2. InfluxDB)
    - En la página en el campo Token selecciona Reset 
    - Pega el nuevo valor del token
    - Valida la conexión







