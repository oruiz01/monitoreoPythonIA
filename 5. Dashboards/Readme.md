# Creación de dashboards en Grafana

### 1. Ingresamos al portal de Grafana

### 2. Seleccionamos Grafana / Dashboards / + Create dashboards
![image](https://github.com/user-attachments/assets/a8c11fbc-664f-49cf-8e8f-e6573ef28c28)

### 3. Seleccionamos + Add visualization
![image](https://github.com/user-attachments/assets/9c6c9c3a-7b41-41cb-82c3-4793bbf6bbc6)

### 4. Indicamos el datasource a usar: influxdb-sql

### 5. Nos presenta la siguiente salida
![image](https://github.com/user-attachments/assets/a2682e9e-0a44-400f-9bdd-07be3976b833)

### 6. Instalamos un plugin para mensajes de texto
Seleccionamos Grafana / Administration / Plugins and data / Plugins
  ![image](https://github.com/user-attachments/assets/0b95039b-b708-486a-a3b4-668702d6cd41)

Buscamos y seleccionamos Bussiness Text 

  ![image](https://github.com/user-attachments/assets/9c471851-defe-48b8-bae9-1ea8c56e6232)

Seleccionamos Install
  ![image](https://github.com/user-attachments/assets/c3f3a0ee-1c3e-48ab-aaae-78f34bda2c7a)

### 7. Creamos Dashboard de tipo texto
Ingresamos a Grafana / Dashboards / Reportes / Add / Visualization
  ![image](https://github.com/user-attachments/assets/a5f1a65d-3f51-40a2-b16c-d020b46dfe43)

Buscamos y seleccionamos Bussiness Text
  ![image](https://github.com/user-attachments/assets/8f2664c0-de02-44be-9f0a-5d5f1d11bf53)

En la parte inferior seleccionamos Code
  ![image](https://github.com/user-attachments/assets/180af592-5dcf-4167-94df-6b56f0b53464)

Anexamos la siguiente consulta
```sql
SELECT totaldocumentos FROM "documentos" order by time desc limit 1
```

Seleccionamos Run Query 
Nos presenta la siguiente salida
  ![image](https://github.com/user-attachments/assets/1ea3fab6-c1e8-418c-ad94-c6d654054a07)

Reajustamos las siguiente propiedades
Title:  Total de documentos 
  ![image](https://github.com/user-attachments/assets/eaabba37-7822-4fe0-b1c1-f293252d84f3)

Bajo Content Partials reajustamos la salida
Anexamos: &lt;h1&gt;{{totaldocumentos}} &lt;/h1&gt;
  ![image](https://github.com/user-attachments/assets/6598acc5-bc6e-4ca0-a534-f502afd8f2cd)


Seleccionamos Save dashboards 
  ![image](https://github.com/user-attachments/assets/79d3dd0f-15ec-4e09-9fc6-49e6e238de06)

Proporcionamos el nombre del Dashboard
Seleccionamos Save

  ![image](https://github.com/user-attachments/assets/b23d7936-8b63-4b34-af17-a253ffa2f0da)

Seleccionamos Back to Dashboard
  ![image](https://github.com/user-attachments/assets/9d0ba1b0-95b2-4ff7-b426-807db0d1df79)

Seleccionamos Save Dashboard
  ![image](https://github.com/user-attachments/assets/0d25b725-6fbd-4464-aa1e-fa6595695bab)
