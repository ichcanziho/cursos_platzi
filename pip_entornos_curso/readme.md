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