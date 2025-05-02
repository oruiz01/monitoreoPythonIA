Estas pruebas se realizaron en Ubuntu 24.04
  
1. Validamos que tenemos instalado Python 3

2. Descargamos Anaconda:  https://www.anaconda.com/download/success 

3. Instalamos Anaconda
  chmod 750 Anaconda3-2024.10-1-Linux-x86_64.sh
  ./Anaconda3-2024.10-1-Linux-x86_64.sh

4. Desactivamos ambiente de default
   conda config --set auto_activate_base false
   
5. Creamos un ambiente virtual
   conda create -n virtualenv python=3.11 notebook=7.3.2
   conda activate virtualenv
  
7. Instalamos los prerrequisitos
   chmod 750 requerimientos.sh
   sh requerimientos.sh
   
8. Ingresamos a la carpeta de ejemplos
   cd labs
  
10. Ejecutamos Jupyther
   jupyter notebook --NotebookApp.max_buffer_size=10737418240 --NotebookApp.iopub_data_rate_limit=10737418240



  
