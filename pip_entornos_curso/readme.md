# Clase 1: Python en tu propio entorno de desarrollo local

------------------------------------


Indica nuestra ruta actual
```bash
pwd
```

Crea una carpeta llamada **c1_python_local**
```bash
mkdir c1_python_local
```
Desplegamos la lista de archivos
```bash
ll
```
Nos cambiamos a la carpeta **c1_python_local**
```bash
cd c1_python_local
```
Limpiamos la consola
```bash
clear
```

Iniciamos el proyecto en Git
```bash
git init
```
Creamos un archivo de python
```bash
touch main.py
```

# Clase 2: Instalación de Windows (WSL) y Linux

------------------------------------

### instalación de python
```bash
sudo apt update
sudo apt -y upgrade
```

### Verificar versión de python

```bash
python3 -V
```

### Inslatador de paquetes de pytho Pip

```bash
sudo apt install -y python3-pip
```

### Verificar versión de pip instalada

```bash
pip3 -V
```

### Dependencias en entorno profesional

```bash
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
```

# Clase 4: Python con VSCode

------------------------------------

Instalar VSCode
```bash
sudo snap install --classic code
```

Abrir visual estudio code desde terminal
```bash
code .
```

Instalar la extensión de python de Microsoft

![estructura](./imgs/im1.png "Extensión de python")  

# Clase 5: Python con Git y GitHub

------------------------------------

Paso 1: Creamos un repositorio en GitHub con un nombre de proyecto
![estructura](./imgs/im2.png "Creación de repositorio GitHub")  

Paso 2: Inicializando el repositorio de Git

```bash
git init
```

Esto crea la carpeta oculta de git para hacer tracking de los cambios *.git*

Enlazamos el repositorio externo de GitHub

```bash
git remote add origin (enlace gitgub)
```

Verificar el enlace con GitHub

```bash
git remote -v
```

Agregamos todos los cambios a Git

```bash
git add .
```

Hacemos un commit de los cambios

```bash
git commit -m "Mi primer commit"
```

Subimos los archivos del commit a GitHub

```bash
git push origin master
```

#### Creemos nuestro .gitignore con ayuda de:

https://www.toptal.com/developers/gitignore/

![estructura](./imgs/im3.png "Página para crear gitignores")  

Ahora creamos un archivo Readme

```bash
touch README2.MD
```

# Clase 6: Flujo de Trabajo en Python

------------------------------------

Vamos a copiar el juego de piedra papel o tijera

```bash
mkdir c6_game
cd c6_game
touch main.py
```

Copiamos el código en main.py y ahora lo ejecutamos

```bash
cd c6_game
python3 main.py
```

El readme debe contener todo lo necesario para indicar como debe ser ejectuado el código. Incluyento instalación de dependencias por ejemplo.

# Clase 7: ¿Qué es pip?

-----------
PIP es el gestor de paquetes de python, es posible buscar librerías en la pagina [pypi](https://pypi.org/)

En esta clase veremos como hacer una gráfica con [Matplotlib](https://pypi.org/project/matplotlib/)

```bash
mkdir c7_charts
cd c7_charts
touch main.py
touch charts.py
```

_los códigos de main.py y charts.py han sido copiados y ya estan puestos_

Ahora instalemos la libreria de plotting preferida

```bash
pip3 install matplotlib
```

Si queremos observar todas las librerias instaladas entonces podemos usar:

```bash
pip3 freeze
```

Ejecutemos nuestro código de python

```bash
cd c7_charts
python3 main.py
```

# Clase 8: Gŕaficas en Python con Pip

```bash
mkdir c8_charts_advance
cd c8_charts_advance
```

Está clase es conceptualmente igual a la anterior, no se agrega mucha información.

# Clase 9: ¿Qué es un ambiente virtual?

----------

Los ambientes virtuales en python encapsulan cada uno de los modulos y lo atan a cada proyecto y no lo dejan de forma compartida.

Esto es muy útil cuando tenemos varios proyectos complejos que 
tienen versiones específicas de ciertas dependencias con ciertas versiones. Entonces algun proyecto necesita 
matplotlib 3.6 y otra necesita 3.5, para no tener que instalar y desinstalar los modulos podemos crear entornos virtuales.

# Clase 10: Usando entornos virtuales en Python

Verificar dónde está python y pip
```bash
which python3
which pip
```
Instalar el gestor de entornos virtuales venv en linux

```bash
sudo apt install -y python3-venv
```
Alternativamente
```bash
pip install virtualenv
```

Creando un entorno virtual llamado env:
```bash
python3 -m venv env_c10
```

Activando el ambiente virtual
```bash
source env_c10/bin/activate
```
Como acabamos de crear este entorno virtual, entonces es virgen y no tiene ninguna dependencia instalada, eso lo podemos verificar observando sus dependencias.
```bash
pip freeze
```
Instalemos una dependencia:

```bash
pip install pandas
```
Si volvemos a observar las dependencias ahora vemos la siguiente salida:

```
numpy==1.24.1
pandas==1.5.2
python-dateutil==2.8.2
pytz==2022.7
six==1.16.0
```

Podemos instalar una versión específica de una dependencia de la siguiente manera:

```bash
pip install matplotlib==3.5.0
```

Finalmente, vamos a desactivar el entorno virtual
```bash
deactivate
```

# Clase 11: Requirements.txt

---------------------

Cuando tenemos un proyecto con varias dependendcias es buena idea crear un archivo de requerimientos en el que se enliste todos y cada uno de las dependencias que necesita el proyecto para poder ejecutarse.
A este archivo de dependencias se le conoce como requirements y suele ser un archivo en formato .txt. Este archivo gestiona las
dependencias y sus versiones instaladas.

Primero debemos tener activado nuestro entorno virtual del cuál queremos crear su archivo de dependencias requirements.txt
```bash
source env_c10/bin/activate
```

Con el entorno virtual activo recordemos que podemos observar todas sus dependencias con:
```bash
pip freeze
```

Sin embargo, para generar el archivo txt es tan sencillo como usar el operador de salida "*>*"
```bash
pip freeze > c10_venvs/requirements.txt
cat c10_venvs/requirements.txt
```

Teniendo el archivo de dependencias es muy sencillo instalar todos y cada uno de estas dependencias y modulos. De nuevo es
idóneo crear un nuevo entorno virtual antes de instalar los requisitos. 

```bash
pip install -r requirements.txt
```

Ahora ya podemos correr cualquier archivo del proyecto.

El flujo general de trabajo será el siguiente:

```bash
git clone <nombre_del_repositorio>
cd <nombre_de_la_carpeta_principal>
python3 -m venv <nombre_del_venv>
source <nombre_del_venv>/bin/activate
pip install -r requirements.txt
python main.py
```

# Clase 12: Solicitudes HTTP Con Requests

-----------

Creemos primero un nuevo entorno virtual para este pequeño proyecto

```bash
cd c12_requests
python3 -m venv request_env
source request_env/bin/activate
```

Instalemos nuestra dependencia principal de este proyecto

```bash
pip install requests
```

Ahora crearemos nuestro archivo de requirements

```bash
pip freeze > requirements.txt
```

# Clase 13: Pandas

------

En esta clase solamente se habló un poquito de la librería de pandas, no es muy útil para este específico curso.

Esta clase solo fue mencionada para hablar de la instalación de pandas en el venv

```bash
pip install pandas
```

# Clase 14: Web Server con FastAPI

----------------


### FastApi 
Es un framework de Python para crear aplicaciones web rápidas y seguras. Utilice la mejor OpenAPI para definir la interfaz de la aplicación y proporcione un conjunto de herramientas para validar y documentar la API de manera automática.

### Uvicorn 

Es un servidor ASGI (Asynchronous Server Gateway Interface) de alto rendimiento para ejecutar aplicaciones ASGI como FastAPI. Es una alternativa a otros servidores ASGI como Daphne y Hypercorn.
[Documentación de Uvicorn.](https://www.uvicorn.org/)

FastAPI y Uvicorn se utilizan juntos para proporcionar un entorno rápido y fácil de usar para el desarrollo y el uso de aplicaciones web basadas en ASGI.
Teniendo activado nuestro entorno de request, vamos a instalar dos nuevas dependencias:

### Instalando dependencias

```bash
pip install fastapi
pip install "uvicorn[standard]"
```


```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

if __name__ == "__main__":
    app.run()
```

Una vez que se ha terminado de crear el archivo .py de la aplicación API para montarlo con uvicorn se debe hacer lo siguiente:
```
uvicorn <nombre_del_archivo_python>:<nombre_que_pondras_al_proyecto> --reload
uivcorn main:app --reload
uvicorn main:app --reload
```

Se espera la siguiente respuesta:

```
INFO:     Will watch for changes in these directories: ['/home/gabriel/Documentos/python/platzi/pip_entornos_curso/c14_webserver']
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [15748] using WatchFiles
INFO:     Started server process [15750]
INFO:     Waiting for application startup.
INFO:     Application startup complete.

```

# Clase 15: ¿Qué es Docker?

--------------------

Supongamos que estás trabajando en un proyecto de aplicación web con un equipo de desarrolladores. Cada desarrollador tiene su propia computadora y cada uno está utilizando un sistema operativo diferente (Windows, MacOS o Linux). Además, cada uno de ellos tiene diferentes versiones de las herramientas y bibliotecas necesarias para desarrollar la aplicación.

Con Docker, puedes crear un contenedor que incluya todo lo necesario para ejecutar la aplicación, incluyendo el código, las herramientas y las bibliotecas. Luego, cada desarrollador puede ejecutar la aplicación en su propia computadora simplemente instalando Docker y ejecutando el contenedor. De esta manera, cada uno de los desarrolladores puede trabajar en el mismo entorno, sin importar el sistema operativo o las herramientas que tenga instaladas.

Cuando esté lista para desplegar la aplicación en producción, puedes subir el contenedor a un repositorio de Docker y luego ejecutarlo en cualquier servidor que tenga Docker instalado. De esta manera, puedes asegurarte de que la aplicación funcione de la misma manera en todos los entornos, desde el desarrollo hasta la producción.

# Clase 16: Instalación de Docker Engine en Ubuntu

[Instalacion paso a paso](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

### Set up the repository

Update the apt package index and install packages to allow apt to use a repository over HTTPS:

```
sudo apt-get update
sudo apt-get install \
    ca-certificates \
    curl \
    gnupg \
    lsb-release
```
Add Docker’s official GPG key:
```
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
```
Use the following command to set up the repository:
```
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```
### Install Docker Engine
```
sudo apt-get update
```
Receiving a GPG error when running apt-get update?
```
sudo chmod a+r /etc/apt/keyrings/docker.gpg
sudo apt-get update
```
Install Docker Engine, containerd, and Docker Compose.
```
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin
```
Verify that the Docker Engine installation is successful by running the hello-world image:
```
sudo docker run hello-world
```
Excpected Answer:

```
Unable to find image 'hello-world:latest' locally
latest: Pulling from library/hello-world
2db29710123e: Pull complete 
Digest: sha256:94ebc7edf3401f299cd3376a1669bc0a49aef92d6d2669005f9bc5ef028dc333
Status: Downloaded newer image for hello-world:latest

Hello from Docker!
This message shows that your installation appears to be working correctly.

To generate this message, Docker took the following steps:
 1. The Docker client contacted the Docker daemon.
 2. The Docker daemon pulled the "hello-world" image from the Docker Hub.
    (amd64)
 3. The Docker daemon created a new container from that image which runs the
    executable that produces the output you are currently reading.
 4. The Docker daemon streamed that output to the Docker client, which sent it
    to your terminal.

To try something more ambitious, you can run an Ubuntu container with:
 $ docker run -it ubuntu bash

Share images, automate workflows, and more with a free Docker ID:
 https://hub.docker.com/

For more examples and ideas, visit:
 https://docs.docker.com/get-started/

```

Clase 17: Dockerizando scripts de python

---------------

En esta clase y como pequeño proyecto de ejemplo crearemos un conversor de tipos de archivo estructurados utilizando
la librería de Pandas, entre los archivos que se pueden convertir estan: csv, xlsx, json, xml.

Ya teniendo el código vamos a explicar todo el proceso de dockerizado con python

primero debemos crear un archivo:

```
Dockerfile
```
El cual tendrá adentro la siguiente información:

```
FROM python:3.10
WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY . /app
CMD bash -c "while true; do sleep 1; done"
```
Explicación:

FROM python:3.10 > Voy a utilizar el docker que contiene Python 3.10

WORKDIR /app > El docker tendrá una carpeta raíz llamada app

COPY requirements.txt /app/requirements.txt > copiare el archivo local de requirements.txt a la ruta del docker /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt > Dentro del docker instalaré todas las dependencias necesarias de python

COPY . /app > Copiaré todo el contenido de mi carpeta raíz . a la carpeta raíz de docker app

CMD bash -c "while true; do sleep 1; done" > Mantendré el docker activo

El siguiente archivo a crear es:


```
docker-compose.yml
```

El cuál contiene:

```
services:
  app-convertor:
    build:
      context: .
      dockerfile: Dockerfile
    volumes:
      - .:/app
```

Lo único importante es que: app-convertor - es el nombre que uno elige para su aplicación docker

Teniendo los archivos preparados es momento de empezar con el proceso de dockerizado. 

```
sudo docker compose build
```

Respuesta esperada:
```
 => => transferring context: 165.48MB                                                                                                                                                                                                                                                                              1.0s
 => [2/5] WORKDIR /app                                                                                                                                                                                                                                                                                             0.0s
 => [3/5] COPY requirements.txt /app/requirements.txt                                                                                                                                                                                                                                                              0.0s
 => [4/5] RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt                                                                                                                                                                                                                                       13.6s
 => [5/5] COPY ./ app                                                                                                                                                                                                                                                                                              1.1s
 => exporting to image                                                                                                                                                                                                                                                                                             1.1s
 => => exporting layers                                                                                                                                                                                                                                                                                            1.1s
 => => writing image sha256:b2aceb4d34d05c4fa1353b377e0ab81a7fb1338070e39276e1e2b170bce1c371 
```

Levantamos el contenedor:

```
sudo docker compose up -d
```

Checamos el estado del mismo:

```
sudo docker compose ps
```

Respuesta esperada:
```
NAME                                IMAGE                             COMMAND                  SERVICE             CREATED             STATUS              PORTS
c17_simple_docker-app-convertor-1   c17_simple_docker-app-convertor   "/bin/sh -c 'bash -c…"   app-convertor       27 seconds ago      Up 26 seconds 
```
Ahora vamos a entrar el docker compose:

```
sudo docker compose exec app-convertor bash
```

Podemos observar todos los archivos que se encuentran en nuestro docker file:

```
ls -l
```
Respuesta esperada:
```
-rw-rw-r-- 1 root root  199 Jan 10 20:39 Dockerfile
-rw-rw-r-- 1 root root  669 Jan 10 20:02 README.MD
drwxrwxr-x 5 root root 4096 Jan 10 20:33 conversor_env
drwxrwxr-x 3 root root 4096 Jan 10 20:33 core
-rw-rw-r-- 1 root root   85 Jan 10 20:31 docker-compose.yml
-rw-rw-r-- 1 root root  611 Jan 10 19:54 main.py
-rw-rw-r-- 1 root root  136 Jan 10 19:54 requirements.txt
-rw-rw-r-- 1 root root   54 Jan 10 20:00 test.csv
-rw-rw-r-- 1 root root  103 Jan 10 19:39 test.json
-rw-rw-r-- 1 root root 4974 Jan 10 18:56 test.xlsx
-rw-rw-r-- 1 root root  281 Jan 10 18:57 test.xml
-rw-rw-r-- 1 root root   54 Jan 10 19:52 test_name.csv
```

si quiero abrir un archivo para verlo:
```
cat main.py
```

Como ahora todo ya está listo y funcionando, entonces podemos ejecutar el código python:


```bash
python main.py test.csv json -n c_json
```

Salimos de docker:

```bash
exit
```

Verificamos que sigue corriendo el contenedor:

```bash
sudo docker compose ps
```
Podemos exportar el contenedor para compartirlo a otros
```bash
sudo docker export c17_simple_docker-app-convertor-1 > app-convertor.tar
```
Detenemos el container
```bash
sudo docker compose down
```

Y si tenemos un container en formato .tar, podemos importarlo con el siguiente código:
```bash
sudo docker import my-container.tar my-image:latest
```

Para ver una lista de todos los contenedores activos e inactivos:

```bash
sudo docker ps -a
```

Otra forma similar:
```bash
sudo docker images
```

Respuesta esperada:
```
CONTAINER ID   IMAGE                             COMMAND                  CREATED              STATUS                        PORTS     NAMES
7b329a5041b2   c17_simple_docker-app-convertor   "/bin/sh -c 'bash -c…"   About a minute ago   Exited (137) 24 seconds ago             c17_simple_docker-app-convertor-1
f7ff6602f4f6   hello-world                       "/hello"                 6 hours ago          Exited (0) 6 hours ago                  thirsty_elbakyan
```

Detener un container por su id:

```bash
sudo docker stop 7b329a5041b2
```

Error starting userland proxy: listen tcp4 0.0.0.0:80: bind: address already in use


sudo apt install net-tools
sudo netstat -nlptu | grep 80

tcp6       0      0 :::80                   :::*                    ESCUCHAR    853/apache2 

sudo apachectl stop

AH00558: apache2: Could not reliably determine the server's fully qualified domain name, using 127.0.1.1. Set the 'ServerName' directive globally to suppress this message

sudo apachectl start
