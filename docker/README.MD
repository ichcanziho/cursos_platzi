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

## 2.2 Conceptos fundamentales de Docker: contenedores

## 2.3 Comprendiendo el estado de Docker

## 2.4 El modo interactivo

## 2.5 Ciclo de vida de un contenedor

## 2.6 Exponiendo contenedores


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