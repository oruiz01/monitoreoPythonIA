# Configuración de ambiente Python

Estas pruebas se realizaron en Ubuntu 24.04
  
### 1. Descargamos Anaconda:  

    https://www.anaconda.com/download/success 

### 2. Instalamos Anaconda
    
    chmod 750 Anaconda3-2024.10-1-Linux-x86_64.sh
    ./Anaconda3-2024.10-1-Linux-x86_64.sh

### 3. Desactivamos ambiente de default
   
     conda config --set auto_activate_base false
   
### 4. Creamos un ambiente virtual
   
     conda create -n virtualenv python=3.11 notebook=7.3.2
     conda activate virtualenv
    


  
