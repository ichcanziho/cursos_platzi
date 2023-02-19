# Curso de DOCKER

## Tabla de contenidos:

### [1. Introducción](#1-introducción)
### [2. Contenedores](#2-contenedores)
### [3. Datos en Docker](#3-datos-en-docker)
### [4. Imágenes](#4-imágenes)
### [5. Docker como herramienta de desarrollo](#5-docker-como-herramienta-de-desarrollo)
### [6. Docker compose](#6-docker-compose)
### [7. Docker Avanzado](#7-docker-avanzado)


# 1. Introducción

## 1.1 Todo lo que aprenderás sobre Docker

**¿Qué es docker?**

Docker es un programa de código abierto que permite que una aplicación Linux y sus dependencias se empaqueten como un contenedor.

La virtualización basada en contenedores aísla las aplicaciones entre sí en un sistema operativo (OS) compartido. 
Este enfoque estandariza la entrega del programa de la aplicación, permitiendo que las aplicaciones se ejecuten en 
cualquier entorno Linux, ya sea físico o virtual. Dado que comparten el mismo sistema operativo, los contenedores son 
portátiles entre diferentes distribuciones de Linux, y son significativamente más pequeños que las imágenes de máquinas 
virtuales (VM).

**CheatSheet**

![cheatsheet](imgs/cheatsheet.webp)


## 1.2 Las treas áreas en el desarrollo de software profesional

> Docker te permite construir, distribuir y ejecutar cualquier aplicación en cualquier lado.

![problemas](imgs/3problemas.png)

**Problemáticas del desarrollo de software**

1. `Construir` - Escribir código en la máquina del desarrollador. (Compile, que no compile, arreglar el bug, compartir código, etc. )

    - **Problemática:**

      - Entorno de desarrollo (paquetes)
      - Dependencias (Frameworks, bibliotecas)
      - Versiones de entornos de ejecución (runtime, versión Node)
      - Equivalencia de entornos de desarrollo (compartir el código)
      - Equivalencia con entornos productivos (pasar a producción)
      - Servicios externos (integración con otros servicios ejem: base de datos)
2. `Distribuir` - Llevar la aplicación donde se va a desplegar (Transformarse en un artefacto)

   - **Problemática:**

     - Output de build heterogeneous (múltiples compilaciones)
     - Acceso a servidores productivos (No tenemos acceso al servidor)
     - Ejecución nativa vs virtualizada
     - Entornos Serverless
3. `Ejecutar` - Implementar la solución en el ambiente de producción (Subir a producción)
El reto Hacer que funcione como debería funcionar (la máquina donde se ejecuta será diferente a la máquina dónde se diseñó)

   - **Problemática:**

     - Dependencia de aplicación (paquetes, runtime)
     - Compatibilidad con el entorno productivo (sistema operativo poco amigable con la solución)
     - Disponibilidad de servicios externos (Acceso a los servicios externos)
     - Recursos de hardware (Capacidad de ejecución - Menos memoria, procesador más débil)

**¡La respuesta a todos estos problemas es docker!**

![respuesta](imgs/dockergoal.png)

## 1.3 Virtualización

Es la versión virtual de algún recurso tecnológico ya sea hardware, software, el concepto de una máquina ETC.
Permite atacar en simultáneo los tres problemas del desarrollo de software profesional.

**Problemas de las máquinas virtuales:**

- `PESO:` En el orden de los GBs. Repiten archivos en común. Inicio lento.
- `COSTO DE ADMINISTRACION:` Necesita mantenimiento igual que cualquier otra computadora.
- `MULTIPLES DE FORMATO:` VDI, VMDK, VHD, raw, etc (como se empaquetan los vms)
 
Docker ofrece una alternativa de solución a las VMs que evita los problemas anteriormente mencionados, haciendo uso de
`contenedores`.

**Containerization**

A diferencia de la virtualización de una VM las cual es la versión virtual de una máquina, computador o servidor. 
Un contenedor solamente virtualiza lo estrictamente necesario para que el código sea ejecutado.

El concepto de contenedores nace de un problema de la industria del transporte de mercancía marítima, en el cual anteriormente 
era muy difícil transportar mercancía por lo cual se crearon containers los cuales facilitaron el transporte de los 
artículos de una manera más segura que los métodos empleados en esa época. Al usar containers su principal uso es la construcción y despliegue del software.

> La containerization es el empleo de contenedores para construir y desplegar software.

**Ventajas de los contenedores:**
- `flexibles:` cualquier aplicación que quieras meter en un contenedor se puede meter en un contenedor.
- `livianos:` reutilizar kernel para ejecutar el código sin necesidad de tener un sistema operativo completo.
- `portables:` se pueden ejecutar en cualquier máquina, tranquilo están diseñados para eso.
- `bajo acoplamiento:` tiene todo lo necesario para correr el código que está dentro de sí mismo sin necesidad de afectar a otros contenedores.
- `escalables:` se pueden crear varios contenedores sin el temor de que esto afecte el rendimiento o funcionamiento de los mismos.
- `seguros:` solo puede acceder a lo necesario para ejecutar el código. Un contenedor no puede acceder a otro contenedor, ni al sistema operativo que lo ejecuta.


**Virtualization vs Containerization**

![contenedores_vs_vms](imgs/contenedores_vs_vms.png)

`Virtualization:` A diferencia de un contenedor, las máquinas virtuales ejecutan un sistema operativo completo, incluido su propio kernel.
`Containerization:` Un contenedor es un silo aislado y ligero para ejecutar una aplicación en el sistema operativo host. 

Los contenedores se basan en el kernel del sistema operativo host (que puede considerarse la fontanería del sistema operativo), 
y solo puede contener aplicaciones y algunas API ligeras del sistema operativo y servicios que se ejecutan en modo de usuario.


## 1.4 Preparando tu entorno de trabajo

[Instalación paso a paso](https://docs.docker.com/engine/install/ubuntu/#install-using-the-repository)

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
Expected Answer:

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

## 1.5 Play with Docker

[Play with docker](https://labs.play-with-docker.com/#)

Play with docker es una página web que te permite tener acceso a una máquina virtual que contiene docker instalado

![play1](imgs/pwd1.png)

Para empezar a usar docker es tán simple como crear una nueva instancia de docker dentro de la máquina virtual.

Cabe resaltar que todo lo que hagamos en play with docker tiene un tiempo máximo de duración de 4 horas, después de ese tiempo
todas las sesiones e instancias de docker serán eliminadas.

![play2](imgs/pwd2.png)

Una vez que creamos una nueva instancia, nos otorgan una máquina virtual con 4 GiB de memoria RAM y una terminal de linux con 
varios de los programas más útiles para desarrollar, como por ejemplo Git y obviamente una versión de Docker que podemos
comprobar con el comando 
> docker --version
> 

![play3](imgs/pwd3.png)

## 1.6 Qué es y cómo funciona Docker

Docker es una plataforma que permite construir, ejecutar y compartir aplicaciones mediante contenedores.

![engine](imgs/DockerEngine.png)


**Componentes DENTRO del círculo de Docker:**

- `Docker daemon:` Es el centro de docker, el corazón que gracias a él, podemos comunicarnos con los servicios de docker.
- `REST API:` Como cualquier otra API, es la que nos permite visualizar docker de forma “gráfica”.
- `Cliente de docker:` Gracias a este componente, podemos comunicarnos con el corazón de docker (Docker Daemon) que por defecto es la línea de comandos.

**Dentro de la arquitectura de Docker encontramos:**

- `Contenedores:` Es la razón de ser de Docker, es donde podemos encapsular nuestras imágenes para llevarlas a otra computadora, o servidor, etc.
- `Imágenes:` Son las encapsulaciones de x contenedor. Podemos correr nuestra aplicación en Java por medio de una imagen, podemos utilizar Ubuntu para correr nuestro proyecto, etc.
- `Volúmenes de datos:` Podemos acceder con seguridad al sistema de archivos de nuestra máquina.
- `Redes:` Son las que permiten la comunicación entre contenedores.

La arquitectura Docker es una arquitectura cliente-servidor, dónde el cliente habla con el servidor (que es un proceso daemon)
mediante un API para poder gestionar el ciclo de vida de los contenedores y así poder construir, ejecutar y distribuir los contenedores.

El hecho de que el cliente se comunique con el servidor mediante el API hace que el cliente y servidor puedan estar en 
la misma máquina comunicándose mediante sockets de UNIX o bien en máquinas diferentes comunicándose mediante un end-point en la red.

![ejemplo_docker](imgs/ejemplo_docker.jpg)

Docker está escrito en GO, aunque también se aprovecha de muchas de las capacidades del kernel Linux, como namespaces, cgroups, y el sistema de ficheros UnionFS.

Dentro de los elementos de la Arquitectura Docker encontramos dos, por un lado, el elemento principal de la arquitectura Docker que es el Docker Engine y por otro el Registro Docker.

**Docker Engine**

El Docker Engine es la aplicación cliente-servidor que implementa Docker. Esta aplicación tiene tres componentes:

1. `Servidor:` es el proceso principal de Docker y que funciona como proceso demonio del sistema. Es el encargado de gestionar los objetos que hay en Docker como imágenes, contenedores, redes y volúmenes. Se representa mediante el comando dockerd.
2. `API Rest:` es un API Rest que nos permite acceder a las capacidades del servidor y ejecutar comandos sobre él. Podemos utilizar un simple curl para acceder a las capacidades del API de Docker
3. `Cliente`: es la línea de comandos representada por el comando docker. El cliente habla vía el API Rest para poder ejecutar los comandos. Es lo que utilizaremos para poder ir gestionando el ciclo de vida de nuestras imágenes y contenedores.

**Registros Docker**

Los registros Docker (Docker Registry) son los que almacenan imágenes Docker. El Docker Hub es un registro público que almacena múltiples imágenes, algunas de ellas certificadas por Docker.

# 2. Contenedores

## 2.1 Primeros pasos: Hola mundo

Intentemos nuestro primer hola mundo utilizando docker

> docker run hello-world

Es probable que nos arroje el siguiente error:

```commandline
ocker: permission denied while trying to connect to the Docker daemon socket at unix. connect: permission denied.
See 'docker run --help'.
```
Para resolver el error debemos correr el comando con permisos de superusuario

> sudo docker run hello-world

La respuesta esperada es entonces:

```
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

## 2.2 Conceptos fundamentales de Docker: contenedores

Docker es un software que nos ayuda en el proceso del desarrollo de software, solucionando problemas en diferentes 
aspectos como lo son la construcción, distribución y ejecución mediante el concepto de contenedores

Un contenedor la unidad logica más importante de docker que permite encapsular las dependencias de un proyecto en un 
entorno aislado, con esto puedes conseguir resolver el problema de “But it works in my machine”, ya que te permite 
crear una especie de máquina virtual y pasársela a tus compañeros o colocarlo en un servidor para el despliegue de 
manera fácil.

`¡Alerta!` Puedes ver a un contendor como una máquina virtual, pero eso no significa que lo sea, una máquina virtual 
puede llegar a ser muy similar debido a sus funcionalidades como el aislamiento de procesos.

Entonces… **¿Cuál es el beneficio de usar contenedores en lugar de máquinas virtuales?**

El mayor beneficio es que los contenedores de Docker están en el nivel de los MB eso nos da ventajas en el consumo de 
recursos, ya que estos corren compartiendo el host del kernel de Linux, por otro lado, las máquinas virtuales son un 
sistema operativo(O.S) con sus propias apps que corre sobre el tuyo usando virtualización y que consume muchos recursos 
en el nivel de los GB. Una mejor forma de ver esto es observando la arquitectura de los contendores y de las máquinas virtuales

> ## Resumen el bullets

- El concepto de contenedor es uno de los más importantes en el mundo de Docker
- El contenedor será el lugar donde se correrán nuestras aplicaciones
- Un contenedor se podría entender como una máquina virtual liviana
  - Una máquina virtual es un programa que corre en una máquina, pero tiene un sistema operativo, propia memoria, interfaces de red, etc. Es decir, que todo lo que tiene una computadora es virtualizado.
- Un contenedor es una agrupación de procesos que corren nativamente en la máquina, pero están aislados del resto del sistema
- Un contenedor es una unidad lógica, no como una máquina virtual, que es una agrupación física aunque virtualizada que tiene abstracciones de memoria, CPU, etc.
- Al ser una agrupación lógica puede correr de manera nativa en la máquina anfitriona
  - Dicha agrupación está limitada a que cosas acceder y ver de la máquina anfitriona
- Lo que corre adentro de un contenedor, realmente cree que está en la máquina virtual, representada por el contenedor.
  - Es decir que no puede ver más allá de lo que permitamos

> **RESUMEN:** A fines prácticos, un contenedor es como una máquina virtual, para el software que deseemos correr. 
> Lo que caracteriza a un contenedor es que se hace sencillo definir los alcances que tendrá cada contenedor, es liviano y corre de manera nativa.

Un contenedor es una instancia ejecutable de una imagen. Puede crear, iniciar, detener, mover o eliminar un contenedor 
mediante la API o la CLI de Docker. Puede conectar un contenedor a una o más redes, adjuntarle almacenamiento o incluso 
generar una nueva imagen basada en su estado actual.

De forma predeterminada, un contenedor está relativamente bien aislado de otros contenedores y de su máquina host. 
Puede controlar qué tan aislados están la red, el almacenamiento u otros subsistemas subyacentes de un contenedor de 
otros contenedores o de la máquina host.

Un contenedor se define por su imagen, así como por las opciones de configuración que le proporcione al crearlo o 
iniciarlo. Cuando se quita un contenedor, cualquier cambio en su estado que no esté almacenado en el almacenamiento 
persistente desaparece.
[Referencia.](https://docs.docker.com/get-started/overview/)

**Características de unos contendores:**

- Los contenedores: son una agrupación de procesos que se encuentran dentro de una entidad lógica.
- Los contenedores están aislados, y tienen recursos limitados.
- Los contenedores ejecutan procesos de forma nativa en linux.
- Los contenedores se pueden ver como máquinas virtuales livianas y aisladas.
- Cada contenedor tiene un ID único, también tiene un nombre


Para limitar los recursos que un contenedor usa, lo podemos hacer desde su creación (cuando corremos el comando docker run) usando flags de:
Runtime constraints on resources

```
docker run --memory="100m" --cpus=0.5 <image>
```

## 2.3 Comprendiendo el estado de Docker

``` bash
# Hola mundo con docker
$ docker run hello-world
# Ver contenedores corriendo
$ docker ps
# Ver todos los contenedores
$ docker ps -a
# Inspecionar la config un contenedor
$ docker inspect <container_id or container_name>
# Crear un contenedor con un nombre personalizado
$ docker run --name <custom_name> <image_name>
# Renombrar un contenedor
$ docker rename --name <old_name> <new_name>
# Eliminar un contenedor
$ docker rm <container_id or container_name>
# Eliminar todos los contenedores apagados
$ docker container prune
# Eliminar TODOS los contenedores
$ docker rm -f $(docker ps -aq)
```

> Solucionando: permission denied while trying to connect to the Docker daemon socket at unix

1. Enter the command below to create the docker group on the system.
    ```bash
    sudo groupadd -f docker
    ```
2. Type the following usermod command to add the active user to the docker group.
    ```bash
    sudo usermod -aG docker $USER
    ```
3. Apply the group changes to the current terminal session by typing:
    ```bash
    newgrp docker
    ```
4. Check if the docker group is in the list of user groups.
    ```bash
    groups
    ```

The group appears in the command output.

```commandline
docker adm cdrom sudo dip plugdev lpadmin lxd sambashare ichcanziho
```

1. Para observar la lista de contenedores que hemos creado:

    ```bash
    docker ps -a
    ```
    Valor esperado:
    ```commandline
    CONTAINER ID   IMAGE         COMMAND    CREATED        STATUS                    PORTS     NAMES
    60fe77cefcf9   hello-world   "/hello"   26 hours ago   Exited (0) 26 hours ago             distracted_thompson
    fb6bd4692734   hello-world   "/hello"   27 hours ago   Exited (0) 27 hours ago             musing_knuth
    ```
    Los contenedores pueden ser identificados por su `CONTAINER ID` El cual es un número de identificación generado
    automáticamente por docker, o por `NAMES` el cual es un alias que se genera automáticamente o puede ser seleccionado por el usuario.

2. Creando un contenedor con un nombre personalizado:

    ```bash
    docker run --name ejemplito hello-world
    docker pes -a
    ```

    Respuesta esperada:
    
    ```bash
    CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
    1e29458b4fa2   hello-world   "/hello"   6 seconds ago   Exited (0) 6 seconds ago             ejemplito
    60fe77cefcf9   hello-world   "/hello"   26 hours ago    Exited (0) 26 hours ago              distracted_thompson
    fb6bd4692734   hello-world   "/hello"   28 hours ago    Exited (0) 28 hours ago              musing_knuth
   ```
   
3. Eliminando un contenedor por su nombre:
    ```bash
    docker run rm ejemplito
    docker pes -a
    ```

    Respuesta esperada:
    
    ```bash
    CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
    60fe77cefcf9   hello-world   "/hello"   26 hours ago    Exited (0) 26 hours ago              distracted_thompson
    fb6bd4692734   hello-world   "/hello"   28 hours ago    Exited (0) 28 hours ago              musing_knuth
   ```

4. Eliminando todos los contenedores inactivos:

    ```bash
    docker container prune
    docker pes -a
    ```

    Respuesta esperada:
    
    ```bash
    CONTAINER ID   IMAGE         COMMAND    CREATED         STATUS                     PORTS     NAMES
   ```

## 2.4 El modo interactivo

En esta clase vamos a ver como utilizar un contenedor que tenga una función en específico, para ello primero vamos a descargar
un contenedor de linux `ubuntu`

```bash
docker run ubuntu
```

Respuesta esperada:

```bash
Unable to find image 'ubuntu:latest' locally
latest: Pulling from library/ubuntu
677076032cca: Pull complete 
Digest: sha256:9a0bdde4188b896a372804be2384015e90e3f84906b750c1a53539b585fbbe7f
Status: Downloaded newer image for ubuntu:latest
```

Como no encontró una descarga del contenedor de ubuntu, lo primero que hizo fue buscar un contenedor de ubuntu y descargarlo.
Sin embargo, más allá de eso no parece haber hecho nada el comando, veamos su estado con un `ps -a`

```bash
docker ps -a
```

Respuesta esperada:

```bash
CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS                     PORTS     NAMES
d48c3671d68d   ubuntu    "/bin/bash"   2 minutes ago   Exited (0) 2 minutes ago             thirsty_merkle
```

Vemos que efectivamente se creó un contenedor llamado `thirsty_merkle` sin embargo su estado es `Exited (0)`, esto se debe a que
una vez que se creó el contenedor de ubuntu, el último comando de su creación fue un `/bin/bash` que refiere al comando de salir de
ubuntu. Pero esto no parece muy práctico, para poder entrar a ubuntu y utilizarlo desde dentro debemos entrar al modo interactivo.

Podemos acceder al modo interactivo desde que creamos el contenedor de la siguiente manera:

```bash
docker run -it --name ubuntito ubuntu
```

Respuesta esperada:

```bash
root@3d75f60733ce:/# 
```

Eureka, estamos dentro de linux ubuntu, así que vamos a comprobarlo de la siguiente manera, comprobando la versión de ubuntu
instalada con docker. Para ello corramos el siguiente comando:

```bash
cat /etc/lsb-release
```

Respuesta esperada:

```commandline
DISTRIB_ID=Ubuntu
DISTRIB_RELEASE=22.04
DISTRIB_CODENAME=jammy
DISTRIB_DESCRIPTION="Ubuntu 22.04.1 LTS"
```



Si abrimos otra terminal, podemos ver el estado actual de nuestros contenedores con nuestro comando de siempre:

```bash
docker ps -a
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND       CREATED          STATUS                      PORTS     NAMES
3d75f60733ce   ubuntu    "/bin/bash"   4 minutes ago    Up 4 minutes                          ubuntito
d48c3671d68d   ubuntu    "/bin/bash"   10 minutes ago   Exited (0) 10 minutes ago             thirsty_merkle
```

Vemos como nuestro docker `ubuntito`se encuentra activo y corriendo. 

Para salir de esta versión de ubuntu es tan simple como ejecutar: `exit`

```commandline
root@3d75f60733ce:/# exit
```
Y esto me regresa a mi terminal normal.

## 2.5 Ciclo de vida de un contenedor

Cuando un contenedor se ejecuta lo que en realidad ejecuta es un proceso del sistema operativo. Este proceso determina si 
el contenedor sigue vivo o no en función de si está funcionando o no. Sin embargo, en nuestro último contendor `ubuntito`
su última acción fue `exit` entonces su main process término y por ende el proceso del contenedor termina y sale de la 
ejecución del contenedor. 

Vamos a crear un nuevo contenedor de ubuntu cuyo proceso principal NO SEA `/bin/bash` esto nos va a permitir tener un contenedor
que siempre esté activo mientras su proceso principal se esté ejecutando.

```bash
docker run --name alwaysup -d ubuntu tail -f /dev/null 
docker ps -a
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND               CREATED          STATUS                      PORTS     NAMES
f53ace3b3544   ubuntu    "tail -f /dev/null"   5 seconds ago    Up 5 seconds                          alwaysup
3d75f60733ce   ubuntu    "/bin/bash"           28 minutes ago   Exited (0) 10 minutes ago             ubuntito
```
Lo más importante es resaltar que ahora está corriendo `tail -f /dev/null`

Y entonces, ahora que está corriendo un proceso diferente, entonces cómo entro a este contenedor de ubuntu para hacer algo con él?
Vamos a utilizar la función `exec`

```commandline
docker exec -it <container_id> <action_to_exec>
```
En este específico caso queremos entrar a alwaysup a su terminal bash, entonces ejecutamos el siguiente comando:
```bash
docker exec -it alwaysup bash
```
Perfecto ya estamos dónde antes, dentro de bash de ubuntu
```commandline
root@f53ace3b3544:/# 
```

Y si ahora salimos de ubuntu con `exit` y después vemos los procesos podemos observar lo siguiente:

```bash
exit
docker ps -a
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND               CREATED          STATUS                      PORTS     NAMES
f53ace3b3544   ubuntu    "tail -f /dev/null"   3 minutes ago    Up 3 minutes                          alwaysup
3d75f60733ce   ubuntu    "/bin/bash"           32 minutes ago   Exited (0) 14 minutes ago             ubuntito
```

Always up sigue corriendo como si nada. Para detener el contenedor, tenemos más de una forma, una de ellas, es detener 
el main process que está ejecutando el contenedor alwaysup, porque nosotros ya sabemos que si se detiene este proceso entonces
el contenedor también se detendrá, para ello encontremos el id del main process de alwaysup:

```bash
docker inspect --format '{{.State.Pid}}' alwaysup
```
En mi caso su id es el siguiente `17948`

Desde `linux` el comando para detener el proceso sería:

```bash
kill 17948
```

Otra forma más genérica de detener el contenedor, sin pensar en el main process es:

```commandline
docker stop <container_id or container_name>
```

```bash
docker stop alwaysup
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND               CREATED          STATUS                        PORTS     NAMES
f53ace3b3544   ubuntu    "tail -f /dev/null"   9 minutes ago    Exited (137) 41 seconds ago             alwaysup
3d75f60733ce   ubuntu    "/bin/bash"           38 minutes ago   Exited (0) 19 minutes ago               ubuntito
```

Y a pesar de que always up actualmente se encuentra detenido, como su proceso principal es `tail -f /dev/null`

Puedo volver a utilizarlo, simplemente encendiendo el contenedor con `docker start` y volviendo a ejecutar en modo interactivo

```bash
docker start alwaysup
docker exect -it alwaysup bash
```

## 2.6 Exponiendo contenedores


1. Para exponer un contenedor se debe habilitar un puerto para que escuche las solicitudes que se le hacen al contenedor, nginx para este caso práctico trae un puerto habilitado que es el 80 y tiene un proceso encendido por defecto

2. Luego a ese puerto del contenedor se le debe asociar a un puerto de la máquina hosts

3. Adicionalmente, visualizar los logs de peticiones

Crear un contenedor partiendo de una imagen de nginx Asociar un puerto de un contenedor a una máquina hosts
Ejecución del paso 1 y 2

```commandline
$ sudo docker run -d --name <nombre contenedor> -p <puerto hosts>:<puerto contenedor>    <imagen> 

	-d or --detach : 
		Inicia un contenedor sin asociar el input/output del contenedor al terminal.
	-name: 
		asigna un nombre a nuestra contenedor, localmente

	-p: 
		publish,  asocia el puerto hosts con el puerto del contenedo
```

Ejemplo:

```bash
sudo docker run -d --name proxy -p 8080:80 nginx 
```

Respuesta esperada:

```commandline
Unable to find image 'nginx:latest' locally
latest: Pulling from library/nginx
bb263680fed1: Pull complete 
258f176fd226: Pull complete 
a0bc35e70773: Pull complete 
077b9569ff86: Pull complete 
3082a16f3b61: Pull complete 
7e9b29976cce: Pull complete 
Digest: sha256:6650513efd1d27c1f8a5351cbd33edf85cc7e0d9d0fcb4ffb23d8fa89b601ba8
Status: Downloaded newer image for nginx:latest
e4064d4de0b9f063094e6f6d764549a05e0e0911ea4cc6ad1dcb354913f09122
```

Veamos nuestros contenedores:

```bash
docker ps -a
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                        PORTS                                   NAMES
e4064d4de0b9   nginx     "/docker-entrypoint.…"   36 seconds ago   Up 35 seconds                 0.0.0.0:8080->80/tcp, :::8080->80/tcp   proxy
f53ace3b3544   ubuntu    "tail -f /dev/null"      25 minutes ago   Exited (137) 14 minutes ago                                           alwaysup
3d75f60733ce   ubuntu    "/bin/bash"              54 minutes ago   Exited (0) 35 minutes ago                                             ubuntito
```

Lo importante a resaltar es que ahora tenemos un contenedor llamado proxy con un puente de puertos, que usa el puerto de mi
computadora 8080 con el puerto 80 del contenedor.

y si en mi navegador voy a [localhost:8080](localhost:8080)

![nginx](imgs/nginx.png)

**Visualizar los logs**

Ejecución del paso 3

```commandline
$ sudo  docker logs <nombre contenedor>
$ sudo  docker logs -f  <nombre contenedor>
$ sudo  docker logs --tail 10 -f <nombre contenedor

	-f:
		Follow, conecta input/output de nuestra termianl
	--tail n:
		Muestra las n lineas en la terminal
```

Ejemplo:

```bash
$ sudo docker logs proxy
$ sudo docker logs -f proxy
$ sudo docker logs --tail 10 -f proxy
```

Respuesta esperada:

```commandline
172.17.0.1 - - [19/Feb/2023:04:29:18 +0000] "GET / HTTP/1.1" 200 615 "-" "Mozilla/5.0 (X11; Linux x86_64) 
AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"
2023/02/19 04:29:18 [error] 30#30: *2 open() "/usr/share/nginx/html/favicon.ico" failed (2: No such file or directory), 
client: 172.17.0.1, server: localhost, request: "GET /favicon.ico HTTP/1.1", host: "localhost:8080", referrer: 
"http://localhost:8080/"
172.17.0.1 - - [19/Feb/2023:04:29:18 +0000] "GET /favicon.ico HTTP/1.1" 404 555 "http://localhost:8080/" "Mozilla/5.0 
(X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36" "-"
```

Si detengo el contenedor proxy

```bash
docker stop proxy
docker ps -a
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND                  CREATED             STATUS                        PORTS     NAMES
e4064d4de0b9   nginx     "/docker-entrypoint.…"   6 minutes ago       Exited (0) 37 seconds ago               proxy
f53ace3b3544   ubuntu    "tail -f /dev/null"      31 minutes ago      Exited (137) 20 minutes ago             alwaysup
3d75f60733ce   ubuntu    "/bin/bash"              About an hour ago   Exited (0) 41 minutes ago               ubuntito
```
Puedo observar que Ya no tengo puertos disponibles y si intento ir a [localhost:8080](localhost:8080)
ahora me da un error de que no se puede acceder a este sitio.

![ngn_error](imgs/nginx_error.png)

Bastaría con volver a iniciar el contenedor con `docker start proxy` para volver a utilizar nginx.

# 3. Datos en Docker

## 3.1 Bind mounts

## 3.2 Volúmenes

## 3.3 Insertar y extraer archivos de un contenedor

# 4. Imágenes

## 4.1 Conceptos fundamentales de Docker: Imágenes

## 4.2 Construyendo una imagen propia

## 4.3 El sistema de capas

# 5. Docker como herramienta de desarrollo

## 5.1 Usando Docker para desarrollar aplicaciones

## 5.2 Aprovechando el caché de capas para estructurar correctamente tus imágenes

## 5.3 Docker networking: Colaboración entre contenedores

# 6. Docker compose

## 6.1 Docker Compose: La herramienta todo en uno

## 6.2 Subcomandos de Docker Compose

## 6.3 Docker Compose como herramienta de desarrollo

## 6.4 Compose en equipo: override

# 7. Docker Avanzado

## 7.1 Administrando tu ambiente de Docker

## 7.2 Deteniendo contenedores correctamente: SHELL vs EXEC

## 7.3 Contenedores ejecutables: ENTRYPOINT vs CMD

## 7.4 El contexto de build

## 7.5 Multi-stage build

## 7.6 Docker-in-Docker