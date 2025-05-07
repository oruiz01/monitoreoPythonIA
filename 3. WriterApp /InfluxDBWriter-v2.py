### Archivo:        InfluxDBWriter-v2.py
### Versión:        1.0
### Autor:          Oscar Ruiz / oscarruiz@ciencias.unam.mx
### Fecha:          México, 7 de mayo 2025
### Observaciones:
###     Este código es una prueba de concepto.

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
