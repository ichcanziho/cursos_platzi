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

Muchas veces necesitamos acceder a datos en nuestros contenedores que se encuentran por fuera de ellos mismos. Sin embargo, 
directamente los contenedores de docker no saben que se encuentran contenidos, y para ellos todo el universo que existe
solo se encuentra dentro de lo que alcanzan a ver (el propio contenedor). En esta clase veremos una forma en la cual podemos
compartir información y datos que existen fuera del contenedor al contenedor. 

Para empezar con el ejemplo creemos un contenedor que contenga una base de datos de Mongo:

```bash
docker run -d --name mongo_db mongo
```

Respuesta esperada:

```commandline
Unable to find image 'mongo:latest' locally
latest: Pulling from library/mongo
10ac4908093d: Pull complete 
685504455d09: Pull complete 
ebd36404f329: Pull complete 
3abd9b25affb: Pull complete 
2d7fde532eae: Pull complete 
24fc70e4c7d7: Pull complete 
ffc2353072f7: Pull complete 
560de8e3a6c7: Pull complete 
0748cd1d792c: Pull complete 
Digest: sha256:2374c2525c598566cc4e62145ba65aecfe1bd3bf090cccce1ca44f3e2b60f861
Status: Downloaded newer image for mongo:latest
798c3fe2cb6f6578ffcb0626984a6eeb8325952ee91e8e21c220a2a026dbd798
```

Obsevemos el estado de nuestros contenedores:

```bash
docker ps -a
```

Respuesta esperada:

```commandline
CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS                      PORTS       NAMES
798c3fe2cb6f   mongo     "docker-entrypoint.s…"   36 seconds ago   Up 35 seconds               27017/tcp   mongo_db
e4064d4de0b9   nginx     "/docker-entrypoint.…"   18 hours ago     Exited (0) 18 hours ago                 proxy
f53ace3b3544   ubuntu    "tail -f /dev/null"      18 hours ago     Exited (137) 18 hours ago               alwaysup
3d75f60733ce   ubuntu    "/bin/bash"              19 hours ago     Exited (0) 19 hours ago                 ubuntito
```

Excelente ya tenemos un contenedor de mongo llamado `mongo_db`

Entremos al contenedor con el comando `exec` de forma iterativa

```bash
docker exec -it mongo_db bash
```

Ahora supongamos que queremos crear una base de datos llamada `platzi` y crear  un schema llamado `users` donde almacenemos 
el nombre de los usuarios.

Para ello estando dentro del contenedor de `mongo_db`

Ejecutamos el siguiente comando: `mongosh`

```bash
root@798c3fe2cb6f:/# mongosh
```

Respuesta esperada:

```commandline
Current Mongosh Log ID:	63f2a2e7630523f5d94c34be
Connecting to:		mongodb://127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&appName=mongosh+1.6.2
Using MongoDB:		6.0.4
Using Mongosh:		1.6.2

For mongosh info see: https://docs.mongodb.com/mongodb-shell/


To help improve our products, anonymous usage data is collected and sent to MongoDB periodically (https://www.mongodb.com/legal/privacy-policy).
You can opt-out by running the disableTelemetry() command.

------
   The server generated these startup warnings when booting
   2023-02-19T22:24:27.100+00:00: Using the XFS filesystem is strongly recommended with the WiredTiger storage engine. See http://dochub.mongodb.org/core/prodnotes-filesystem
   2023-02-19T22:24:27.303+00:00: Access control is not enabled for the database. Read and write access to data and configuration is unrestricted
   2023-02-19T22:24:27.303+00:00: vm.max_map_count is too low
------

------
   Enable MongoDB's free cloud-based monitoring service, which will then receive and display
   metrics about your deployment (disk utilization, CPU, operation statistics, etc).
   
   The monitoring data will be available on a MongoDB website with a unique URL accessible to you
   and anyone you share the URL with. MongoDB may use this information to make product
   improvements and to suggest MongoDB products and deployment options to you.
   
   To enable free monitoring, run the following command: db.enableFreeMonitoring()
   To permanently disable this reminder, run the following command: db.disableFreeMonitoring()
```

Podemos listar a nuestras bases de datos actuales:

```bash
test> show dbs
```

Respuesta esperada:

```commandline
admin   40.00 KiB
config  12.00 KiB
local   40.00 KiB
```

Y ahora creamos una nueva llamada `platzi`

```bash
test> use platzi
```

Respuesta esperada:

```commandline
switched to db platzi
```

Y ahora en el schema `users`agreguemos el nombre de Gabriel a la columna `nombre`:

```bash
platzi> db.users.insert({"nombre": "Gabriel"}
```

Respuesta esperada:

```commandline
DeprecationWarning: Collection.insert() is deprecated. Use insertOne, insertMany, or bulkWrite.
{
  acknowledged: true,
  insertedIds: { '0': ObjectId("63f2a331babefe10bec0f55c") }
}
```

Y para observar que el dato se encuentra correctamente grabado:

```bash
platzi> db.users.find()
```

Respuesta esperada:

```commandline
[ { _id: ObjectId("63f2a331babefe10bec0f55c"), nombre: 'Gabriel' } ]
```

Sin embargo, si nosotros ahora detuviéramos el contenedor y lo borraremos, si volviéramos a crear un nuevo contenedor mongodb
y quisiéramos crear la dbs `platzi` está sería completamente nueva y nuestros datos de la base anterior no existirían, puesto
que esta es una nueva instancia de mongo db es un contenedor completamente aislado del anterior.

Eliminemos la base `mongo_db`

```bash
docker rm -f mongo_db
```
Ahora lo que vamos a hacer es una carpeta especial que esté espejada y que lo qué existe en esta carpeta también se vea de 
la misma manera dentro de un contenedor.

Primero vamos a crear una carpeta llamada `mongo_db` que usaremos para hacerla espejo más adelante.

```bash
mkdir mongo_db
```

Lo primero que necesito es la ruta completa de dónde se encuentra mi carpeta `mongodata`:

```bash
pwd
```

Respuesta esperada:

```commandline
/home/ichcanziho/Documentos/programacion/cursos_platzi/docker/dockerdata
```

Entonces ahora vamos a crear de nuevo el contenedor de mongo pero con un data bind de la carpeta dockerdata:

```bash
docker run -d --name mongo_db -v /home/ichcanziho/Documentos/programacion/cursos_platzi/docker/dockerdata/mongo_db:/data/db mongo
```

Después del parámetro -v debe ir la ruta completa de la carpeta local : ruta de la carpeta dentro del contenedor.

Entramos al contenedor:

```bash
docker exec -it mongo_db bash
mongosh
use platzi
db.users.insert({"nombre": "Gabriel"})
db.users.find()
exit 
exit
```
Y puedo volver a eliminar el contenedor:
```bash
docker rm -f mongo_db
```

Ahora dentro de dockerdata tengo una carpeta llamada `mongo_db` que tiene toda la información que genero el contenedor anterior.

Si ahora vuelvo a crear el contenedor:

```bash
docker run -d --name mongo_db -v /home/ichcanziho/Documentos/programacion/cursos_platzi/docker/dockerdata/mongo_db:/data/db mongo
docker exec -it mongo_db bash
mongosh
use cursos_platzi
db.users.find()
```

Ahora sí se encontraran mis datos disponibles:

```commandline
[ { _id: ObjectId("63f2a9d2850faa3a35505028"), nombre: 'Gabriel' } ]
```

## 3.2 Volúmenes

Una alternativa bastante eficiente y más segura es usar volúmenes, pues estos los gestiona directamente Docker y solo son visibles
por el administrador y no tienes necesidad de estar enlazando carpetas entre la máquina local y el contenedor docker.

> Nota de seguirada: Ojo que el contenido de los volúmenes “aministrados por Docker” sí se puede acceder desde fuera… Simplemente hay que hacer docker volume inspect VOLUME_NAME, ahí aparecerá el “Mountpoint” del volumen (path en el disco local), y si nos dirigimos allí (con usuario administrador o sudo en sistemas UNIX) podremos ver todo el contenido y gestionarlo.

Los volúmenes son el mecanismo preferido para conservar los datos generados y utilizados por los contenedores de Docker. 
Si bien los montajes de enlace dependen de la estructura del directorio y el sistema operativo de la máquina host, 
Docker administra completamente los volúmenes. Los volúmenes tienen varias ventajas sobre los montajes vinculantes:

**Ventajas**

- Mayor seguridad al compartir archivos entre contenedores, los archivos los maneja directamente docker esto implica que, cualquier persona no puedes acceder a estos archivos.
- Los volúmenes son más fáciles de respaldar o migrar que enlazar montajes.
- Puede administrar volúmenes mediante los comandos de la CLI de Docker o la API de Docker.
- Los volúmenes funcionan tanto en contenedores de Linux como de Windows.
- Los volúmenes se pueden compartir de forma más segura entre varios contenedores.
- Los controladores de volumen le permiten almacenar volúmenes en hosts remotos o proveedores en la nube, para cifrar el contenido de los volúmenes o para agregar otras funciones.
- Los nuevos volúmenes pueden tener su contenido pre cargado por un contenedor.
- Los volúmenes en Docker Desktop tienen un rendimiento mucho mayor que los montajes de enlace de hosts de Mac y Windows.
- Además, los volúmenes suelen ser una mejor opción que los datos persistentes en la capa de escritura de un contenedor, porque un volumen no aumenta el tamaño de los contenedores que lo usan y el contenido del volumen existe fuera del ciclo de vida de un contenedor determinado.

**Desventajas**
- Una de las desventajas es que si se desea visualizar los archivos desde la máquina hosts es mucho más complicado.


### Pasos para conservar datos fuera de los contenedores con volúmenes.

1. Crear el volumen
2. verificar que el volumen fue creado
3. crear un nuevo contenedor basado en una imagen de mongo e indicarle que guardará o usará los datos de un volumen
4. Es opcional, pero se puede inspeccionar el contenedor para visualizar si el volumen quedo configurado.
5. Acceder al bash de nuestro contenedor,
6. Acceder a mongo
7. Crear un base de datos y usarla
8. Realizar una inserción de datos en la base de datos
9. Confirmar la inserción en la base de datos
10. Salir del contenedor
11. borrar contenedor.

### Pasos para crear un nuevo contenedor y usar un volumen anteriormente creado.

1. Crear un nuevo contenedor basado en una imagen de mongo e indicarle que guardará o usará los datos de un volumen anteriormente creado
2. Acceder al bash de nuestro contenedor,
3. Acceder a mongo
4. Usar la bases de datos creadas
5. Confirmar la inserción en la base de datos, que fue realizada anteriormente

### Ejecución de los pasos para conservar datos fuera de los contenedores con usando volúmenes

```bash
$ sudo docker volume create dbdata
$ sudo docker volume ls
$ sudo docker run -d --name db --mount src=dbdata,dst=/data/db mongo
$ sudo docker inspect db
$ sudo docker exec -it db bash
$ mongosh
use platzi

db.users.insert({“nombre”:“guido”})

db.users.find()

$ exit
sudo docker rm -f
```

### Ejecución de los pasos para crear un nuevo contenedor y usar un volumen anteriormente creado.

```bash
$ sudo docker run -d --name db --mount src=dbdata,dst=/data/db mongo
$ sudo docker exec -it db bash
$ mongosh
show dbs
use platzi

db.users.find()
```

### Explicación de los comandos de volumen

```commandline
parámetros

	<nombre c>: 
		nombre del contenedor, así se llamará localmente
<path L>: 
	directorio local
<path C>: 
	directorio del contenedor
< nombre i>:
	nombre de la imagen

flag
--name: 
	asigna un nombre de forma local a nuestro contenedor
-d or --detach: 
	Inicia un contenedor sin asociar el input/output del contenedor al terminal.
    --mount  src =<volume F>,dst=<Carpeta d>:
	Se indica  el  src es igual al volumen fuente, dst es igual a la carpeta destino, es decir a la carpeta del contenedor donde se genera los datos 
```

Ejemplo:

```commandline
$ sudo docker run -d --name db --mount  src =dbdata,dst=/data/db mongo
```

Crear un volumen

```commandline
$ sudo docker volume create <nombre de volumen>
```

```commandline
volume create:
	Crear volumen 
<nombre de volumen>:
	Nombre Volumen
```

Ejemplo:

```commandline
$ sudo docker volume create dbdata
```

![docker_vol](imgs/comandos_volumen.webp)


## 3.3 Insertar y extraer archivos de un contenedor

Independientemente de si usamos bind mounts, o volúmenes, muchas veces queremos poder compartir archivos desde nuestra máquina 
anfitriona a nuestro contenedor, esto es lo que veremos en esta clase.

![temp_files](imgs/temp_files.webp)

- `Host:` Donde Docker esta instalado.
- `Bind Mount:` Guarda los archivos en la máquina local persistiendo y visualizando estos datos (No seguro).
- `Volume:` Guarda los archivos en el área de Docker donde Docker los administra (Seguro).
- `TMPFS Mount:` Guarda los archivos temporalmente y persiste los datos en la memoria del contenedor, cuando muera sus datos mueren con el contenedor.

Ahora hagamos un ejercicio rápido de transferencia de archivos entre máquina local y contenedor.

1. Creamos un archivo de texto vació:
   ```bash
   touch prueba.txt
   ```
2. Creamos un contenedor de ubuntu que se mantenga corriendo:
    ```bash
   docker run -d --name copytest ubuntu tail -f /dev/null
   docker ps -a
   ```
   Respuesta esperada:
   ```commandline
    CONTAINER ID   IMAGE     COMMAND                  CREATED          STATUS          PORTS       NAMES
    b87515bed57b   ubuntu    "tail -f /dev/null"      13 seconds ago   Up 12 seconds               copytest
    9a21d22678d1   mongo     "docker-entrypoint.s…"   24 minutes ago   Up 24 minutes   27017/tcp   mongodb
    ```
3. Entramos dentro del contenedor de ubuntu:
    ```bash
   docker exec -it copytest bash
   ```
4. Creo una carpeta dentro del directorio principal de ubuntu:
    ```bash
    mkdir testing 
   ll
    ```
   Respuesta esperada:
    ```commandline
    total 60
    drwxr-xr-x   1 root root 4096 Feb 20 17:00 ./
    drwxr-xr-x   1 root root 4096 Feb 20 17:00 ../
    -rwxr-xr-x   1 root root    0 Feb 20 16:57 .dockerenv*
    lrwxrwxrwx   1 root root    7 Jan 26 02:03 bin -> usr/bin/
    drwxr-xr-x   2 root root 4096 Apr 18  2022 boot/
    drwxr-xr-x   5 root root  340 Feb 20 16:57 dev/
    drwxr-xr-x   1 root root 4096 Feb 20 16:57 etc/
    drwxr-xr-x   2 root root 4096 Apr 18  2022 home/
    lrwxrwxrwx   1 root root    7 Jan 26 02:03 lib -> usr/lib/
    lrwxrwxrwx   1 root root    9 Jan 26 02:03 lib32 -> usr/lib32/
    lrwxrwxrwx   1 root root    9 Jan 26 02:03 lib64 -> usr/lib64/
    lrwxrwxrwx   1 root root   10 Jan 26 02:03 libx32 -> usr/libx32/
    drwxr-xr-x   2 root root 4096 Jan 26 02:03 media/
    drwxr-xr-x   2 root root 4096 Jan 26 02:03 mnt/
    drwxr-xr-x   2 root root 4096 Jan 26 02:03 opt/
    dr-xr-xr-x 500 root root    0 Feb 20 16:57 proc/
    drwx------   2 root root 4096 Jan 26 02:06 root/
    drwxr-xr-x   5 root root 4096 Jan 26 02:06 run/
    lrwxrwxrwx   1 root root    8 Jan 26 02:03 sbin -> usr/sbin/
    drwxr-xr-x   2 root root 4096 Jan 26 02:03 srv/
    dr-xr-xr-x  13 root root    0 Feb 20 16:57 sys/
    drwxr-xr-x   2 root root 4096 Feb 20 17:00 testing/
    drwxrwxrwt   2 root root 4096 Jan 26 02:06 tmp/
    drwxr-xr-x  14 root root 4096 Jan 26 02:03 usr/
    drwxr-xr-x  11 root root 4096 Jan 26 02:06 var/
    ```
5. Ahora puedo salir de la máquina de ubuntu para estar en la terminal principal
    ```bash
   exit
    ```

6. Vamos a copiar nuestro archivo `prueba.txt` a la carpeta `testing` del contenedor `copytest`:
    ```commandline
    docker cp <archivo a copiar> <nombre o id del contenedor>:<ruta a donde copiar>/<nuevo nombre del archivo>
    ```
    ```bash
   docker cp prueba.txt copytest:/testing/test.txt 
   ```

7. Verificamos que la copia del archivo fue exitosa:
    ```bash
    docker exec -it copytest bash
   cd testing
   ll
   ```
   Respuesta esperada:
    ```commandline
    total 8
    drwxr-xr-x 2 root root 4096 Feb 20 17:02 ./
    drwxr-xr-x 1 root root 4096 Feb 20 17:02 ../
    -rw-rw-r-- 1 1000 1000    0 Feb 20 16:55 test.txt
    ```
   Salimos del contenedor
    ```bash
   exit
    ```
8. Finalmente, veremos como pasar datos de dentro del contenedor a nuestra máquina local:
    ```commandline
    docker cp <nombre o id del contenedor>:<ruta a carpeta o archivo a copiar> <ruta de destino>
    ```
   Ejemplo:
    ```bash
   docker cp copytest:/testing localtesting
    ```   

9. Verificando que los datos se hayan copiado correctamente a nuestra máquina local:
   ```bash
   ll 
   ```
   Respuesta esperada:
    ```commandline
    drwxrwxr-x  5 ichcanziho ichcanziho  4096 feb 20 11:09 ./
    drwxrwxr-x 10 ichcanziho ichcanziho  4096 feb 16 11:35 ../
    drwxrwxr-x  3 ichcanziho ichcanziho  4096 feb 19 17:05 dockerdata/
    drwxrwxr-x  2 ichcanziho ichcanziho  4096 feb 20 10:51 imgs/
    drwxr-xr-x  2 ichcanziho ichcanziho  4096 feb 20 11:02 localtesting/
    -rw-rw-r--  1 ichcanziho ichcanziho     0 feb 20 10:55 prueba.txt
    -rw-rw-r--  1 ichcanziho ichcanziho 48633 feb 20 11:08 README.MD
    ```
   Verificando archivos copiados:
   ```bash
   cd localtesting
   ll 
   ```
   Respuesta esperada:
    ```commandline
    drwxr-xr-x 2 ichcanziho ichcanziho 4096 feb 20 11:02 ./
    drwxrwxr-x 5 ichcanziho ichcanziho 4096 feb 20 11:09 ../
    -rw-rw-r-- 1 ichcanziho ichcanziho    0 feb 20 10:55 test.txt
    ```

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